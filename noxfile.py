"""Nox configuration for development tasks."""

import json
import os
import re
from pathlib import Path

import nox
import tomli
from nox.command import CommandFailed

nox.options.reuse_existing_virtualenvs = True
nox.options.default_venv_backend = "uv"

NOT_SKIP_WITH_ACT = "not skip_with_act"
LATEXMK_VERSION_MIN = 4.86
LICENSES_JSON_PATH = "reports/licenses.json"
SBOM_CYCLONEDX_PATH = "reports/sbom.json"
SBOM_SPDX_PATH = "reports/sbom.spdx"


def _setup_venv(session: nox.Session, all_extras: bool = True) -> None:
    """Install dependencies for the given session using uv."""
    args = ["uv", "sync", "--frozen"]
    if all_extras:
        args.append("--all-extras")
    session.run_install(
        *args,
        env={
            "UV_PROJECT_ENVIRONMENT": session.virtualenv.location,
            "UV_PYTHON": str(session.python),
        },
    )


def _is_act_environment() -> bool:
    """Check if running in GitHub ACT environment.

    Returns:
        bool: True if running in ACT environment, False otherwise.
    """
    return os.environ.get("GITHUB_WORKFLOW_RUNTIME") == "ACT"


@nox.session(python=["3.13"])
def lint(session: nox.Session) -> None:
    """Run code formatting checks, linting, and static type checking."""
    _setup_venv(session)
    session.run("ruff", "check", ".")
    session.run(
        "ruff",
        "format",
        "--check",
        ".",
    )
    session.run("mypy", "src")


@nox.session(python=["3.13"])
def audit(session: nox.Session) -> None:
    """Run security audit and license checks."""
    _setup_venv(session, True)

    # pip-audit to check for vulnerabilities
    session.run("pip-audit", "-f", "json", "-o", "reports/vulnerabilities.json")
    session.run("jq", ".", "reports/vulnerabilities.json", external=True)

    # pip-licenses to check for compliance
    pip_licenses_base_args = [
        "pip-licenses",
        "--with-system",
        "--with-authors",
        "--with-maintainer",
        "--with-url",
        "--with-description",
    ]

    # Filter by .license-types-allowed file if it exists
    allowed_licenses = []
    licenses_allow_file = Path(".license-types-allowed")
    if licenses_allow_file.exists():
        allowed_licenses = [
            line.strip()
            for line in licenses_allow_file.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.strip().startswith(("#", "//"))
        ]
        session.log(f"Found {len(allowed_licenses)} allowed licenses in .license-types-allowed")
    if allowed_licenses:
        allowed_licenses_str = ";".join(allowed_licenses)
        session.log(f"Using --allow-only with: {allowed_licenses_str}")
        pip_licenses_base_args.extend(["--partial-match", "--allow-only", allowed_licenses_str])

    # Generate CSV and JSON reports
    session.run(
        *pip_licenses_base_args,
        "--format=csv",
        "--order=license",
        "--output-file=reports/licenses.csv",
    )
    session.run(
        *pip_licenses_base_args,
        "--with-license-file",
        "--with-notice-file",
        "--format=json",
        "--output-file=" + LICENSES_JSON_PATH,
    )

    # Group by license type
    session.run("jq", ".", LICENSES_JSON_PATH, external=True)
    licenses_data = json.loads(Path(LICENSES_JSON_PATH).read_text(encoding="utf-8"))
    licenses_grouped: dict[str, list[dict[str, str]]] = {}
    licenses_grouped = {}
    for pkg in licenses_data:
        license_name = pkg["License"]
        package_info = {"Name": pkg["Name"], "Version": pkg["Version"]}
        if license_name not in licenses_grouped:
            licenses_grouped[license_name] = []
        licenses_grouped[license_name].append(package_info)
    Path("reports/licenses_grouped.json").write_text(
        json.dumps(licenses_grouped, indent=2),
        encoding="utf-8",
    )
    session.run("jq", ".", "reports/licenses_grouped.json", external=True)

    # SBOMs
    session.run("cyclonedx-py", "environment", "-o", SBOM_CYCLONEDX_PATH)
    session.run("jq", ".", SBOM_CYCLONEDX_PATH, external=True)

    # Generates an SPDX SBOM including vulnerability scanning
    session.run(
        "trivy",
        "fs",
        "uv.lock",
        "--include-dev-deps",
        "--scanners",
        "vuln",
        "--format",
        "spdx",
        "--output",
        SBOM_SPDX_PATH,
        external=True,
    )


def _generate_attributions(session: nox.Session, licenses_json_path: Path) -> None:
    """Generate ATTRIBUTIONS.md from licenses.json.

    Args:
        session: The nox session instance
        licenses_json_path: Path to the licenses.json file
    """
    attributions = "# Attributions\n\n"
    attributions += f"[//]: # (This file is generated by make docs from {LICENSES_JSON_PATH})\n\n"

    if not licenses_json_path.exists():
        attributions += "Please run `make audit` first to generate the necessary license information.\n"
        Path("ATTRIBUTIONS.md").write_text(attributions, encoding="utf-8")
        session.log("Generated placeholder ATTRIBUTIONS.md file - run 'make audit' to populate it properly")
        return

    licenses_data = json.loads(licenses_json_path.read_text(encoding="utf-8"))

    attributions += "This project includes code from the following third-party open source projects:\n\n"

    for pkg in licenses_data:
        name = pkg.get("Name", "Unknown")
        version = pkg.get("Version", "Unknown")
        license_name = pkg.get("License", "Unknown")
        authors = pkg.get("Author", "Unknown")
        maintainers = pkg.get("Maintainer", "")
        url = pkg.get("URL", "")
        description = pkg.get("Description", "")

        attributions += f"## {name} ({version}) - {license_name}\n\n"

        if description:
            attributions += f"{description}\n\n"

        if url:
            attributions += f"* URL: {url}\n"

        if authors and authors != "UNKNOWN":
            attributions += f"* Author(s): {authors}\n"

        if maintainers and maintainers != "UNKNOWN":
            attributions += f"* Maintainer(s): {maintainers}\n"

        attributions += "\n"

        license_text = pkg.get("LicenseText", "")
        if license_text and license_text != "UNKNOWN":
            attributions += "### License Text\n\n"
            # Sanitize backtick sequences to not escape the code block
            sanitized_license_text = license_text.replace("```", "~~~")
            attributions += f"```\n{sanitized_license_text}\n```\n\n"

        notice_text = pkg.get("NoticeText", "")
        if notice_text and notice_text != "UNKNOWN":
            attributions += "### Notice\n\n"
            # Sanitize backtick sequences to not escape the code block
            sanitized_notice_text = notice_text.replace("```", "~~~")
            attributions += f"```\n{sanitized_notice_text}\n```\n\n"

    attributions = attributions.rstrip() + "\n"
    Path("ATTRIBUTIONS.md").write_text(attributions, encoding="utf-8")

    session.log("Generated ATTRIBUTIONS.md file")


def _compile_readme(session: nox.Session) -> None:
    """Compile README partial files into a single README.md.

    Args:
        session: The nox session instance
    """
    preamble = "\n[//]: # (README.md generated from docs/partials/README_*.md)\n\n"
    header = Path("docs/partials/README_header.md").read_text(encoding="utf-8")
    main = Path("docs/partials/README_main.md").read_text(encoding="utf-8")
    footer = Path("docs/partials/README_footer.md").read_text(encoding="utf-8")
    readme_content = f"{preamble}{header}\n\n{main}\n\n{footer}"
    Path("README.md").write_text(readme_content, encoding="utf-8")
    session.log("Generated README.md file from partials")


def _dump_openapi_schemas(session: nox.Session) -> None:
    """Dump OpenAPI schemas for different API versions in YAML and JSON formats.

    Args:
        session: The nox session instance
    """
    # Create directory if it doesn't exist
    Path("docs/source/_static").mkdir(parents=True, exist_ok=True)

    try:
        # Generate API v1 schemas
        try:
            with Path("docs/source/_static/openapi_v1.yaml").open("w", encoding="utf-8") as f:
                session.run("oe-python-template-example", "openapi", "--api-version=v1", stdout=f, external=True)
            with Path("docs/source/_static/openapi_v1.json").open("w", encoding="utf-8") as f:
                session.run(
                    "oe-python-template-example",
                    "openapi",
                    "--api-version=v1",
                    "--output-format=json",
                    stdout=f,
                    external=True,
                )
            session.log("Generated API v1 OpenAPI schemas")
        except CommandFailed:
            session.log("Failed to generate API v1 OpenAPI schemas - command may not be supported")

        # Generate API v2 schemas
        try:
            with Path("docs/source/_static/openapi_v2.yaml").open("w", encoding="utf-8") as f:
                session.run("oe-python-template-example", "openapi", "--api-version=v2", stdout=f, external=True)
            with Path("docs/source/_static/openapi_v2.json").open("w", encoding="utf-8") as f:
                session.run(
                    "oe-python-template-example",
                    "openapi",
                    "--api-version=v2",
                    "--output-format=json",
                    stdout=f,
                    external=True,
                )
            session.log("Generated API v2 OpenAPI schemas")
        except CommandFailed:
            session.log("Failed to generate API v2 OpenAPI schemas - command may not be supported")

        session.log("OpenAPI schema generation completed")
    except Exception as e:  # noqa: BLE001
        session.log(f"Warning: Could not generate OpenAPI schemas: {e}")


def _build_pdf_docs(session: nox.Session) -> None:
    """Build PDF documentation using latexmk.

    Args:
        session: The nox session instance

    Raises:
        CommandFailed: If latexmk is not installed or not in PATH
        ValueError: If the installed latexmk version is outdated
        AttributeError: If parsing the latexmk version information fails
    """
    try:
        out = session.run("latexmk", "--version", external=True, silent=True)

        version_match = re.search(r"Version (\d+\.\d+\w*)", str(out))
        if not version_match:
            session.error("Could not determine latexmk version")

        version_str = version_match.group(1)

        # Parse version (handle cases like "4.86a")
        match = re.match(r"(\d+\.\d+)", version_str)
        if not match:
            session.error(f"Could not parse version number from '{version_str}'")
        base_version = match.group(1)

        if float(base_version) < LATEXMK_VERSION_MIN:
            message = f"latexmk version {version_str} is outdated. Please run 'brew upgrade mactex' to upgrade."
            raise ValueError(message)  # noqa: TRY301
        session.log(f"latexmk version {version_str} is sufficient")
        session.run("make", "-C", "docs", "latexpdf", external=True)
        session.log("PDF documentation generated and available at: docs/build/latex/oe-python-template-example.pdf")

    except CommandFailed as e:
        session.error(f"latexmk is not installed or not in PATH: {e}. Please run 'brew install mactex' to install")
    except (ValueError, AttributeError) as e:
        session.error(f"Failed to parse latexmk version information: {e}")


@nox.session(python=["3.13"])
def docs(session: nox.Session) -> None:
    """Build documentation and concatenate README.

    This function performs several documentation-related tasks:
    1. Concatenates partial README files into a single README.md
    2. Dumps OpenAPI schemas (v1 and v2) in both YAML and JSON formats
    3. Builds HTML, single HTML, and LaTeX documentation
    4. Optionally builds PDF documentation if "pdf" is in session arguments

    Args:
        session: The nox session instance

    Raises:
        CommandFailed: If latexmk is not installed or not in PATH
        ValueError: If the installed latexmk version is outdated
        AttributeError: If parsing the latexmk version information fails
    """
    _setup_venv(session)

    _generate_attributions(session, Path(LICENSES_JSON_PATH))
    _compile_readme(session)
    _dump_openapi_schemas(session)

    # Build docs
    session.run("make", "-C", "docs", "clean", external=True)
    session.run("make", "-C", "docs", "html", external=True)
    session.run("make", "-C", "docs", "singlehtml", external=True)
    session.run("make", "-C", "docs", "latex", external=True)

    if "pdf" in session.posargs:
        _build_pdf_docs(session)


@nox.session(python=["3.13"], default=False)
def docs_pdf(session: nox.Session) -> None:
    """Setup dev environment post project creation."""  # noqa: DOC501
    _setup_venv(session)
    try:
        out = session.run("latexmk", "--version", external=True, silent=True)

        version_match = re.search(r"Version (\d+\.\d+\w*)", str(out))
        if not version_match:
            session.error("Could not determine latexmk version")

        version_str = version_match.group(1)

        # Parse version (handle cases like "4.86a")
        match = re.match(r"(\d+\.\d+)", version_str)
        if not match:
            session.error(f"Could not parse version number from '{version_str}'")
        base_version = match.group(1)

        if float(base_version) < LATEXMK_VERSION_MIN:
            message = f"latexmk version {version_str} is outdated. Please run 'brew upgrade mactex' to upgrade."
            raise ValueError(message)  # noqa: TRY301
        session.log(f"latexmk version {version_str} is sufficient")
        session.run("make", "-C", "docs", "latexpdf", external=True)

    except CommandFailed as e:
        session.error(f"latexmk is not installed or not in PATH: {e}. Please run 'brew install mactex' to install")
    except (ValueError, AttributeError) as e:
        session.error(f"Failed to parse latexmk version information: {e}")


@nox.session(python=["3.11", "3.12", "3.13"])
def test(session: nox.Session) -> None:
    """Run tests with pytest."""
    _setup_venv(session)
    pytest_args = ["pytest", "--disable-warnings", "--junitxml=reports/junit.xml", "-n", "auto", "--dist", "loadgroup"]
    if _is_act_environment():
        pytest_args.extend(["-k", NOT_SKIP_WITH_ACT])
    session.run(*pytest_args)


@nox.session(python=["3.13"], default=False)
def setup(session: nox.Session) -> None:
    """Setup dev environment post project creation."""
    _setup_venv(session)
    session.run("ruff", "format", ".", external=True)
    git_dir = Path(".git")
    if git_dir.is_dir():
        session.run("echo", "found .git directory", external=True)
        session.run("touch", ".act-env-secret", external=True)
        session.run("pre-commit", "install", external=True)
        with Path(".secrets.baseline").open("w", encoding="utf-8") as out:
            session.run("detect-secrets", "scan", stdout=out, external=True)
        session.run("git", "add", ".", external=True)
        try:
            session.run("pre-commit", external=True)
        except Exception:  # noqa: BLE001
            session.log("pre-commit run failed, continuing anyway")
        session.run("git", "add", ".", external=True)


@nox.session(default=False)
def update_from_template(session: nox.Session) -> None:
    """Update from copier template."""
    if Path("copier.yaml").is_file() or Path("copier.yml").is_file():
        # Read the current version from pyproject.toml
        with Path("pyproject.toml").open("rb") as f:
            pyproject = tomli.load(f)
            current_version = pyproject["tool"]["bumpversion"]["current_version"]
            # In this case the project itself is the template
            session.run("copier", "copy", "-r", "HEAD", ".", ".", "--force", "--trust", "--skip-tasks", external=True)
            # Bump the version using the current version from pyproject.toml
            session.run("bump-my-version", "replace", "--new-version", current_version, "--allow-dirty", external=True)
    else:
        # In this case the template has been generated from a template
        session.run("copier", "update", "--trust", "--skip-answered", "--skip-tasks", external=True)

    # Schedule the lint session to run after this session completes
    session.notify("audit")
    session.notify("docs")
    session.notify("lint")


@nox.session(default=False)
def act(session: nox.Session) -> None:
    """Run GitHub Actions workflow locally with act."""
    session.run(
        "act",
        "-j",
        "test",
        "--env-file",
        ".act-env-public",
        "--secret-file",
        ".act-env-secret",
        "--container-architecture",
        "linux/amd64",
        "-P",
        "ubuntu-latest=catthehacker/ubuntu:act-latest",
        "--action-offline-mode",
        "--container-daemon-socket",
        "-",
        external=True,
    )


@nox.session(default=False)
def bump(session: nox.Session) -> None:
    """Bump version and push changes to git."""
    version_part = session.posargs[0] if session.posargs else "patch"

    # Check if the version_part is a specific version (e.g., 1.2.3)
    if re.match(r"^\d+\.\d+\.\d+$", version_part):
        session.run("bump-my-version", "bump", "--new-version", version_part, external=True)
    else:
        session.run("bump-my-version", "bump", version_part, external=True)

    # Push changes to git
    session.run("git", "push", external=True)


@nox.session(python=["3.13"])
def dist(session: nox.Session) -> None:
    """Build wheel and put in dist/."""
    _setup_venv(session)
    session.run("uv", "build", external=True)

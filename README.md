# 🧠 OE Python Template Example

[![License](https://img.shields.io/github/license/helmut-hoffer-von-ankershoffen/oe-python-template-example?logo=opensourceinitiative&logoColor=3DA639&labelColor=414042&color=A41831)
](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/blob/main/LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/oe-python-template-example.svg?logo=python&color=204361&labelColor=1E2933)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/blob/main/noxfile.py)
[![CI](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/actions/workflows/test-and-report.yml/badge.svg)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/actions/workflows/test-and-report.yml)
[![Read the Docs](https://img.shields.io/readthedocs/oe-python-template-example)](https://oe-python-template-example.readthedocs.io/en/latest/)
[![Quality Gate](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_oe-python-template-example&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template-example)
[![Security](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_oe-python-template-example&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template-example)
[![Maintainability](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_oe-python-template-example&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template-example)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_oe-python-template-example&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template-example)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=helmut-hoffer-von-ankershoffen_oe-python-template-example&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template-example)
[![CodeQL](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/actions/workflows/codeql.yml/badge.svg)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/security/code-scanning)
[![Dependabot](https://img.shields.io/badge/dependabot-active-brightgreen?style=flat-square&logo=dependabot)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/security/dependabot)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)
[![Coverage](https://codecov.io/gh/helmut-hoffer-von-ankershoffen/oe-python-template-example/graph/badge.svg?token=SX34YRP30E)](https://codecov.io/gh/helmut-hoffer-von-ankershoffen/oe-python-template-example)
[![Ruff](https://img.shields.io/badge/style-Ruff-blue?color=D6FF65)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/blob/main/noxfile.py)
[![MyPy](https://img.shields.io/badge/mypy-checked-blue)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/blob/main/noxfile.py)
[![GitHub - Version](https://img.shields.io/github/v/release/helmut-hoffer-von-ankershoffen/oe-python-template-example?label=GitHub&style=flat&labelColor=1C2C2E&color=blue&logo=GitHub&logoColor=white)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/releases)
[![GitHub - Commits](https://img.shields.io/github/commit-activity/m/helmut-hoffer-von-ankershoffen/oe-python-template-example/main?label=commits&style=flat&labelColor=1C2C2E&color=blue&logo=GitHub&logoColor=white)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/commits/main/)
[![PyPI - Version](https://img.shields.io/pypi/v/oe-python-template-example.svg?label=PyPI&logo=pypi&logoColor=%23FFD243&labelColor=%230073B7&color=FDFDFD)](https://pypi.python.org/pypi/oe-python-template-example)
[![PyPI - Status](https://img.shields.io/pypi/status/oe-python-template-example?logo=pypi&logoColor=%23FFD243&labelColor=%230073B7&color=FDFDFD)](https://pypi.python.org/pypi/oe-python-template-example)
[![Docker - Version](https://img.shields.io/docker/v/helmuthva/oe-python-template-example?sort=semver&label=Docker&logo=docker&logoColor=white&labelColor=1354D4&color=10151B)](https://hub.docker.com/r/helmuthva/oe-python-template-example/tags)
[![Docker - Size](https://img.shields.io/docker/image-size/helmuthva/oe-python-template-example?sort=semver&arch=arm64&label=image&logo=docker&logoColor=white&labelColor=1354D4&color=10151B)](https://hub.docker.com/r/helmuthva/oe-python-template-example/)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTE3IDE2VjdsLTYgNU0yIDlWOGwxLTFoMWw0IDMgOC04aDFsNCAyIDEgMXYxNGwtMSAxLTQgMmgtMWwtOC04LTQgM0gzbC0xLTF2LTFsMy0zIi8+PC9zdmc+)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example)
[![Open in GitHub Codespaces](https://img.shields.io/static/v1?label=GitHub%20Codespaces&message=Open&color=blue&logo=github)](https://github.com/codespaces/new/helmut-hoffer-von-ankershoffen/oe-python-template-example)

<!---
[![ghcr.io - Version](https://ghcr-badge.egpl.dev/helmut-hoffer-von-ankershoffen/oe-python-template-example/tags?color=%2344cc11&ignore=0.0%2C0%2Clatest&n=3&label=ghcr.io&trim=)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/pkgs/container/oe-python-template-example)
[![ghcr.io - Sze](https://ghcr-badge.egpl.dev/helmut-hoffer-von-ankershoffen/oe-python-template-example/size?color=%2344cc11&tag=latest&label=size&trim=)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/pkgs/container/oe-python-template-example)
-->

> [!TIP]
> 📚 [Online documentation](https://oe-python-template-example.readthedocs.io/en/latest/) - 📖 [PDF Manual](https://oe-python-template-example.readthedocs.io/_/downloads/en/latest/pdf/)

> [!NOTE]
> 🧠 This project was scaffolded using the template [oe-python-template](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template) with [copier](https://copier.readthedocs.io/).

---


Example project scaffolded and kept up to date with OE Python Template
(oe-python-template).

Use Cases:

1. Dummy CLI application and service demonstrating example usage of the
   directory structure and build pipeline generated by oe-python-template

## Overview

Adding OE Python Template Example to your project as a dependency is easy.

```shell
uv add oe-python-template-example             # add dependency to your project
```

If you don't have uv installed follow
[these instructions](https://docs.astral.sh/uv/getting-started/installation/).
If you still prefer pip over the modern and fast package manager
[uv](https://github.com/astral-sh/uv), you can install the library like this:

```shell
pip install oe-python-template-example        # add dependency to your project
```

Executing the command line interface (CLI) in an isolated Python environment is
just as easy:

```shell
uvx oe-python-template-example hello-world     # prints "Hello, world! [..]"
uvx oe-python-template-example serve           # serves webservice API
uvx oe-python-template-example serve --port=4711 # serves webservice API on port 4711
```

Notes:
* The API is versioned, mounted at `/api/v1` resp. `/api/v2`
* While serving the webservice API go to [http://127.0.0.1:8000/api/v1/hello-world](http://127.0.0.1:8000/api/v1/hello-world) to see the respons of the `hello-world` operation.
* Interactive documentation is provided at [http://127.0.0.1:8000/api/docs](http://127.0.0.1:8000/api/docs)


The CLI provides extensive help:

```shell
uvx oe-python-template-example --help                # all CLI commands
uvx oe-python-template-example hello-world --help    # help for specific command
uvx oe-python-template-example echo --help
uvx oe-python-template-example openapi --help
uvx oe-python-template-example serve --help
```

## Operational Excellence

This project is designed with operational excellence in mind, using modern
Python tooling and practices. It includes:

- Various examples demonstrating usage:
  - [Simple Python script](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/blob/main/examples/script.py)
  - [Streamlit web application](https://oe-python-template-example.streamlit.app/)
    deployed on [Streamlit Community Cloud](https://streamlit.io/cloud)
  - [Jupyter](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/blob/main/examples/notebook.ipynb)
    and
    [Marimo](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/blob/main/examples/notebook.py)
    notebook
- [Complete reference documentation](https://oe-python-template-example.readthedocs.io/en/latest/reference.html)
  on Read the Docs
- [Transparent test coverage](https://app.codecov.io/gh/helmut-hoffer-von-ankershoffen/oe-python-template-example)
  including unit and E2E tests (reported on Codecov)
- Matrix tested with
  [multiple python versions](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/blob/main/noxfile.py)
  to ensure compatibility (powered by [Nox](https://nox.thea.codes/en/stable/))
- Compliant with modern linting and formatting standards (powered by
  [Ruff](https://github.com/astral-sh/ruff))
- Up-to-date dependencies (monitored by
  [Renovate](https://github.com/renovatebot/renovate) and
  [GitHub Dependabot](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/security/dependabot))
- [A-grade code quality](https://sonarcloud.io/summary/new_code?id=helmut-hoffer-von-ankershoffen_oe-python-template-example)
  in security, maintainability, and reliability with low technical debt and
  codesmell (verified by SonarQube)
- Additional code security checks using
  [GitHub CodeQL](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/security/code-scanning)
- [Security Policy](SECURITY.md)
- [License](LICENSE) compliant with the Open Source Initiative (OSI)
- 1-liner for installation and execution of command line interface (CLI) via
  [uv(x)](https://github.com/astral-sh/uv) or
  [Docker](https://hub.docker.com/r/helmuthva/oe-python-template-example/tags)
- Setup for developing inside a
  [devcontainer](https://code.visualstudio.com/docs/devcontainers/containers)
  included (supports VSCode and GitHub Codespaces)

## Usage Examples

The following examples run from source. Clone this repository first using
`git clone git@github.com:helmut-hoffer-von-ankershoffen/oe-python-template-example.git`.

### Minimal Python Script:

```python
"""Example script demonstrating the usage of the service provided by OE Python Template Example."""

from dotenv import load_dotenv
from rich.console import Console

from oe_python_template_example import Service

console = Console()

load_dotenv()

message = Service.get_hello_world()
console.print(f"[blue]{message}[/blue]")
```

[Show script code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/blob/main/examples/script.py) -
[Read the reference documentation](https://oe-python-template-example.readthedocs.io/en/latest/reference.html)

### Streamlit App

Serve the functionality provided by OE Python Template Example in the web by
easily integrating the service into a Streamlit application.

[Try it out!](https://oe-python-template-example.streamlit.app) -
[Show the code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/blob/main/examples/streamlit.py)

... or serve the app locally

```shell
uv sync --all-extras                                # Install streamlit dependency part of the examples extra, see pyproject.toml
uv run streamlit run examples/streamlit.py          # Serve on localhost:8501, opens browser
```

## Notebooks

### Jupyter

[Show the Jupyter code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/blob/main/examples/notebook.ipynb)

... or run within VSCode

```shell
uv sync --all-extras                                # Install dependencies required for examples such as Juypyter kernel, see pyproject.toml
```

Install the
[Jupyter extension for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

Click on `examples/notebook.ipynb` in VSCode and run it.

### Marimo

[Show the marimo code](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/blob/main/examples/notebook.py)

Execute the notebook as a WASM based web app

```shell
uv sync --all-extras                                # Install ipykernel dependency part of the examples extra, see pyproject.toml
uv run marimo run examples/notebook.py --watch      # Serve on localhost:2718, opens browser
```

or edit interactively in your browser

```shell
uv sync --all-extras                                # Install ipykernel dependency part of the examples extra, see pyproject.toml
uv run marimo edit examples/notebook.py --watch     # Edit on localhost:2718, opens browser
```

... or edit interactively within VSCode

Install the
[Marimo extension for VSCode](https://marketplace.visualstudio.com/items?itemName=marimo-team.vscode-marimo)

Click on `examples/notebook.py` in VSCode and click on the caret next to the Run
icon above the code (looks like a pencil) > "Start in marimo editor" (edit).

## Command Line Interface (CLI)

### Run with [uvx](https://docs.astral.sh/uv/guides/tools/)

Show available commands:

```shell
uvx oe-python-template-example --help
```

Execute commands:

```shell
uvx oe-python-template-example hello-world
uvx oe-python-template-example echo --help
uvx oe-python-template-example echo "Lorem"
uvx oe-python-template-example echo "Lorem" --json
uvx oe-python-template-example openapi
uvx oe-python-template-example openapi --output-format=json
uvx oe-python-template-example serve
```

### Environment

The service loads environment variables including support for .env files.

```shell
cp .env.example .env              # copy example file
echo "THE_VAR=MY_VALUE" > .env    # overwrite with your values
```

Now run the usage examples again.

### Run with Docker

You can as well run the CLI within Docker.

```shell
docker run helmuthva/oe-python-template-example --help
docker run helmuthva/oe-python-template-example hello-world
docker run helmuthva/oe-python-template-example echo --help
docker run helmuthva/oe-python-template-example echo "Lorem"
docker run helmuthva/oe-python-template-example echo "Lorem" --json
docker run helmuthva/oe-python-template-example openapi
docker run helmuthva/oe-python-template-example openapi --output-format=json
docker run helmuthva/oe-python-template-example serve
```

Execute command:

```shell
docker run --env THE_VAR=MY_VALUE helmuthva/oe-python-template-example echo "Lorem Ipsum"
```

Or use docker compose

The .env is passed through from the host to the Docker container.

```shell
docker compose run oe-python-template-example --help
docker compose run oe-python-template-example hello-world
docker compose run oe-python-template-example echo --help
docker compose run oe-python-template-example echo "Lorem"
docker compose run oe-python-template-example echo "Lorem" --json
docker compose run oe-python-template-example openapi
docker compose run oe-python-template-example openapi --output-format=json
docker compose up
curl http://127.0.0.1:8000/api/v1/hello-world
curl http://127.0.0.1:8000/api/v1/docs
curl http://127.0.0.1:8000/api/v2/hello-world
curl http://127.0.0.1:8000/api/v2/docs
```

## Extra: Lorem Ipsum

Nothing yet


## Further Reading

* Check out the [reference](https://oe-python-template-example.readthedocs.io/en/latest/reference.html) with detailed documentation of public classes and functions.
* Our [release notes](https://oe-python-template-example.readthedocs.io/en/latest/release-notes.html) provide a complete log of recent improvements and changes.
* In case you want to help us improve 🧠 OE Python Template Example: The [contribution guidelines](https://oe-python-template-example.readthedocs.io/en/latest/contributing.html) explain how to setup your development environment and create pull requests.

## Star History

<a href="https://star-history.com/#helmut-hoffer-von-ankershoffen/oe-python-template-example">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=helmut-hoffer-von-ankershoffen/oe-python-template-example&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=helmut-hoffer-von-ankershoffen/oe-python-template-example&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=helmut-hoffer-von-ankershoffen/oe-python-template-example&type=Date" />
 </picture>
</a>

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
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://github.com/helmut-hoffer-von-ankershoffen/oe-python-template-example/issues?q=is%3Aissue%20state%3Aopen%20Dependency%20Dashboard)
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

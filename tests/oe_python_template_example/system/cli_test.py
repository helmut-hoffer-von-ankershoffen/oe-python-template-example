"""Tests to verify the CLI functionality of the system module."""

import os
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from oe_python_template_example.cli import cli

THE_VALUE = "THE_VALUE"


@pytest.fixture
def runner() -> CliRunner:
    """Provide a CLI test runner fixture."""
    return CliRunner()


@pytest.mark.scheduled
def test_cli_health(runner: CliRunner) -> None:
    """Check health is true."""
    result = runner.invoke(cli, ["system", "health"])
    assert result.exit_code == 0
    assert "UP" in result.output


def test_cli_info(runner: CliRunner) -> None:
    """Check health is true."""
    result = runner.invoke(cli, ["system", "info"])
    assert result.exit_code == 0
    assert "oe_python_template_example.log" in result.output


def test_cli_info_secrets(runner: CliRunner) -> None:
    """Check secrets only shown if requested."""
    with runner.isolated_filesystem():
        # Set environment variable for the test
        env = os.environ.copy()
        env["OE_PYTHON_TEMPLATE_EXAMPLE_SYSTEM_TOKEN"] = THE_VALUE

        # Run the CLI with the runner
        result = runner.invoke(cli, ["system", "info"], env=env)
        assert result.exit_code == 0
        assert THE_VALUE not in result.output

        # Run the CLI with the runner
        result = runner.invoke(cli, ["system", "info", "--no-filter-secrets"], env=env)
        assert result.exit_code == 0
        assert THE_VALUE in result.output


@patch("uvicorn.run")
def test_cli_serve_no_app(mock_uvicorn_run, runner: CliRunner) -> None:
    """Check serve command starts the server."""
    result = runner.invoke(cli, ["system", "serve", "--host", "127.0.0.1", "--port", "8000", "--no-watch", "--no-app"])
    assert result.exit_code == 0
    assert "Starting webservice API server at http://127.0.0.1:8000" in result.output
    mock_uvicorn_run.assert_called_once_with(
        "oe_python_template_example.api:api",
        host="127.0.0.1",
        port=8000,
        reload=False,
    )


@patch("oe_python_template_example.utils._gui.app.mount")
@patch("oe_python_template_example.utils._gui.ui.run")
@patch("oe_python_template_example.utils._gui.gui_register_pages")
def test_cli_serve_api_and_app(
    mock_register_pages, mock_ui_run, mock_app_mount, runner: CliRunner
) -> None:
    """Check serve command starts the server with API and GUI app."""
    # Create a MagicMock for native_app.find_open_port
    with patch("oe_python_template_example.utils._gui.native_app.find_open_port", return_value=8123):
        result = runner.invoke(cli, ["system", "serve", "--host", "127.0.0.1", "--port", "8000", "--no-watch"])

        assert result.exit_code == 0
        assert "Starting web application server at http://127.0.0.1:8000" in result.output

        # Check that app.mount was called to mount the API
        mock_app_mount.assert_called_once_with("/api", mock_app_mount.call_args[0][1])

        # Check that gui_register_pages was called
        mock_register_pages.assert_called_once()

        # Check that ui.run was called with the correct parameters
        mock_ui_run.assert_called_once_with(
            title="oe_python_template_example",
            favicon="",
            native=False,
            reload=False,
            dark=False,
            host="127.0.0.1",
            port=8000,
            frameless=False,
            show_welcome_message=True,
            show=False,
        )


def test_cli_openapi_yaml(runner: CliRunner) -> None:
    """Check openapi command outputs YAML schema."""
    result = runner.invoke(cli, ["system", "openapi", "--output-format", "yaml"])
    assert result.exit_code == 0
    # Check for common OpenAPI YAML elements
    assert "openapi:" in result.output
    assert "info:" in result.output
    assert "paths:" in result.output
    # Check for specific v1 elements
    assert "Echo:" in result.output

    result = runner.invoke(cli, ["system", "openapi", "--api-version", "v2", "--output-format", "yaml"])
    assert result.exit_code == 0
    # Check for common OpenAPI YAML elements
    assert "openapi:" in result.output
    assert "info:" in result.output
    assert "paths:" in result.output
    # Check for specific v2 elements
    assert "Utterance:" in result.output

    result = runner.invoke(cli, ["system", "openapi", "--api-version", "v3", "--output-format", "yaml"])
    assert result.exit_code == 1
    assert "Error: Invalid API version 'v3'. Available versions: v1, v2" in result.output


def test_cli_openapi_json(runner: CliRunner) -> None:
    """Check openapi command outputs JSON schema."""
    result = runner.invoke(cli, ["system", "openapi"])
    assert result.exit_code == 0
    # Check for common OpenAPI JSON elements
    assert '"openapi":' in result.output
    assert '"info":' in result.output
    assert '"paths":' in result.output


@pytest.mark.scheduled
def test_fail(runner: CliRunner) -> None:
    """Check fails."""
    result = runner.invoke(cli, ["system", "fail"])
    assert result.exit_code == 1


@pytest.mark.scheduled
@pytest.mark.long_running
def test_sleep(runner: CliRunner) -> None:
    """Check sleep."""
    result = runner.invoke(cli, ["system", "sleep"])
    assert result.exit_code == 0

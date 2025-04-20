"""Constants for the OE Python Template Example."""

from pathlib import Path

MODULES_TO_INSTRUMENT = ["oe_python_template_example.hello"]

API_VERSIONS = {
    "v1": "1.0.0",
    "v2": "2.0.0",
}

NOTEBOOK_FOLDER = Path(__file__).parent.parent.parent / "examples"
NOTEBOOK_APP = Path(__file__).parent.parent.parent / "examples" / "notebook.py"

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo",
#     "oe-python-template-example==0.4.1",
# ]
# ///


import marimo
from oe_python_template_example.utils import __version__

__generated_with = "0.13.0"
app = marimo.App(app_title=f"🧠 OE Python Template Example v{__version__}")


@app.cell
def _():
    import marimo as mo
    from oe_python_template_example.hello import Service

    service = Service()
    message = service.get_hello_world()

    with mo.redirect_stdout():
        print(message)
    return


if __name__ == "__main__":
    app.run()

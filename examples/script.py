"""Example script demonstrating the usage of the service provided by OE Python Template Example."""

from dotenv import load_dotenv
from rich.console import Console

from oe_python_template_example import Service

console = Console()

load_dotenv()

message = Service.get_hello_world()
console.print(f"[blue]{message}[/blue]")

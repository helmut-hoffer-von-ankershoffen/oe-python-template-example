"""Example script demonstrating the usage of the service provided by OE Python Template Example."""

from rich.console import Console

from oe_python_template_example.hello import Service

console = Console()

service = Service()

message = service.get_hello_world()
console.print(f"[blue]{message}[/blue]")

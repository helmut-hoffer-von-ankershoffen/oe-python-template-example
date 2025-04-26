"""Example project scaffolded and kept up to date with OE Python Template (oe-python-template)."""

from .constants import MODULES_TO_INSTRUMENT
from .utils.boot import boot

boot(modules_to_instrument=MODULES_TO_INSTRUMENT)

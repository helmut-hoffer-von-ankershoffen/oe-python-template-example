"""
Streamlit web application that demonstrates a simple interface for OE Python Template Example.

This module creates a web interface using Streamlit to demonstrate the usage of the service provided by
OE Python Template Example.
"""

import streamlit as st

from oe_python_template_example import (
    Service,
    __version__,
)

sidebar = st.sidebar
sidebar.write(
    f" [OE Python Template Example v{__version__}](https://oe-python-template-example.readthedocs.io/en/latest/)",
)
sidebar.write("Built with love in Berlin 🐻")

st.title("🧠 OE Python Template Example ")

# Initialize the service
service = Service()

# Get the message
message = service.get_hello_world()

# Print the message
st.write(f"{message}")

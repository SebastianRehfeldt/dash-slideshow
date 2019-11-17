"""Module for reusable Dash components"""
from .table import create_table
from .plot import create_histogram

__all__ = [
    "create_histogram",
    "create_table"
]

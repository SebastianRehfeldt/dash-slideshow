"""Module for creating and adding callbacks"""
from dash import Dash
from .routing import add_routing_callback
from .slide2 import add_slide2_callbacks


def add_callbacks(dash: Dash) -> None:
    """Add all callbacks"""
    add_routing_callback(dash)
    add_slide2_callbacks(dash)

"""Module which contains the slides"""
from typing import Dict, Any
from dash_html_components import Div
from .slide0_overview import create_slide_0
from .slide1_data import create_slide_1
from .slide2_plot import create_slide_2


def get_pages() -> Dict[str, Any]:
    """Return mapping of page names and functions"""
    return {
        "/overview": create_slide_0,
        "/data": create_slide_1,
        "/plot": create_slide_2,
    }


def create_page(url: str) -> Div:
    """Create page based on url"""
    function = get_pages().get(url, None)
    return Div(url) if function is None else function()

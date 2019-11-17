"""Module which contains the slides"""
from dash_html_components import Div
from .slide1_overview import create_slide_1
from .slide2_data import create_slide_2


def create_page(url: str) -> Div:
    """Create page based on url"""
    function = {
        "/overview": create_slide_1,
        "/data": create_slide_2,
    }.get(url, None)
    return Div(url) if function is None else function()

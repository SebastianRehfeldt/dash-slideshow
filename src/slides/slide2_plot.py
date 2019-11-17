"""Overview slide"""
import dash_bootstrap_components as dbc
from dash_html_components import Div, H2


def create_slide_2() -> Div:
    """Returns overview slide with agenda"""
    return dbc.Col([
        H2("Plot example", className="mb-4"),
        Div(id="slide2-plot"),
    ], width=12, className="p-5")

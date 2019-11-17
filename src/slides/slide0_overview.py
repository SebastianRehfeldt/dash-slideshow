"""Overview slide"""
import dash_bootstrap_components as dbc
from dash_html_components import Div, H2, Ol, Li, H5


def create_slide_0() -> Div:
    """Returns overview slide with agenda"""
    return dbc.Col([
        H2("Agenda"),
        H5(Ol([
            Li("Bullet Point 1", className="mt-5"),
            Li("Bullet Point 2"),
            Li("Bullet Point 3"),
            Li("Bullet Point 4"),
        ], className="mt-4 list-spacing"))
    ], width=12, className="p-5")

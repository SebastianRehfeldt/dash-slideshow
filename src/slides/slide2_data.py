"""Overview slide"""
from dash_core_components import Loading
import dash_bootstrap_components as dbc
from dash_html_components import Div, H3, Ul, Li, A


def create_slide_2() -> Div:
    """Returns overview slide with agenda"""
    return dbc.Col([
        H3("Full Datasets", className="mb-4 ml-3"),
        dbc.Card([dbc.CardHeader(
            dbc.Tabs([
                dbc.Tab(label="Airlines", tab_id="slide2-tab-airlines"),
                dbc.Tab(label="Airports", tab_id="slide2-tab-airports"),
                dbc.Tab(label="Flights", tab_id="slide2-tab-flights"),
                dbc.Tab(label="Weather", tab_id="slide2-tab-weather"),
            ], id="slide2-tabs", card=True, active_tab="slide2-tab-airlines")),
            dbc.CardBody(Loading(id="slide2-tab-content"), className="mt-2")
        ]),
    ], width=12, className="mt-5")

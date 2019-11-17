"""Overview slide"""
from dash_core_components import Loading
import dash_bootstrap_components as dbc
from dash_html_components import Div, H2


def create_slide_1() -> Div:
    """Returns overview slide with agenda"""
    return dbc.Col([
        H2("Tabs example", className="mb-4"),
        dbc.Card([dbc.CardHeader(
            dbc.Tabs([
                dbc.Tab(label="Tab 1", tab_id="slide1-tab-1"),
                dbc.Tab(label="Tab 2", tab_id="slide1-tab-2"),
                dbc.Tab(label="Tab 3", tab_id="slide1-tab-3"),
            ], id="slide1-tabs", card=True, active_tab="slide1-tab-1")),
            dbc.CardBody(Loading(id="slide1-tab-content"), className="mt-2")
        ]),
    ], width=12, className="p-5")

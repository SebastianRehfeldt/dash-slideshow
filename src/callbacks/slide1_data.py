"""Routing callback"""
import pandas as pd
from dash import Dash
from dash.dependencies import Input, Output
from dash_html_components import Div
from src.elements import create_table


def update_tab(active_tab: str) -> Div:
    """Return content of active tab"""
    if active_tab == "slide1-tab-1":
        df = pd.DataFrame([[1, 2, 3], [2, 4, 6]], columns=["A", "B", "C"])
        return create_table(df, "slide1-table")
    return Div(active_tab)


def add_slide1_callbacks(dash: Dash) -> None:
    """Add routing callback"""
    dash.callback(
        Output("slide1-tab-content", "children"),
        [Input("slide1-tabs", "active_tab")]
    )(update_tab)

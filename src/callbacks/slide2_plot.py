"""Routing callback"""
import numpy as np
import pandas as pd
from dash import Dash
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from dash_html_components import Div

from src.elements import create_histogram


def update_plot(url: str) -> Div:
    """Return plot"""
    if "plot" not in url:
        raise PreventUpdate

    from time import sleep
    sleep(10000)
    df = pd.DataFrame(np.random.normal(size=10000), columns=["Normal Distribution"])
    return create_histogram(df, "Normal Distribution")


def add_slide2_callbacks(dash: Dash) -> None:
    """Add routing callback"""
    dash.callback(
        Output("slide2-plot", "children"),
        [Input("url", "pathname")]
    )(update_plot)

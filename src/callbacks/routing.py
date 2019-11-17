"""Routing callback"""
from dash import Dash, callback_context
from dash.dependencies import Input, Output, State
from src.slides import create_page


def update_url(_: int, __: int, url: str) -> str:
    """Update url based on buttons"""
    slides = [
        "/overview",
        "/data",
        "/question1",
        "/question2",
        "/question3",
    ]
    if url not in slides:
        return slides[0]

    index = slides.index(url)
    trigger = callback_context.triggered[0]["prop_id"]
    if "prev" in trigger:
        new_index = index - 1 if index > 0 else len(slides) - 1
    if "next" in trigger:
        new_index = index + 1 if index < len(slides) - 1 else 0
    return slides[new_index]


def add_routing_callback(dash: Dash) -> None:
    """Add routing callback"""
    dash.callback(
        Output("row-main", "children"),
        [Input("url", "pathname")]
    )(create_page)

    dash.callback(
        Output("url", "pathname"),
        [Input("btn-next", "n_clicks"),
         Input("btn-prev", "n_clicks")],
        [State("url", "pathname")]
    )(update_url)

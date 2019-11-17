"""Functions to create the main layout"""
from typing import Any
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def get_navbar(title: str) -> dbc.NavbarSimple:
    """Get layout for static navbar"""
    return dbc.NavbarSimple([
        dbc.NavItem(dbc.NavLink("Overview", href="/overview")),
        dbc.DropdownMenu([
            dbc.DropdownMenuItem("Data", href="/data"),
            dbc.DropdownMenuItem("Question 1", href="/question1"),
            dbc.DropdownMenuItem("Question 2", href="/question2"),
            dbc.DropdownMenuItem("Question 3", href="/question3"),
        ], nav=True, in_navbar=True, label="Pages", right=True),
    ], brand=title, brand_href="/overview", color="primary", dark=True, sticky="top")


def serve_layout(title: str) -> Any:
    """Wrapper for layout function to pass title"""

    def _layout() -> html.Div:
        """Function to create layout on each page refresh"""
        return html.Div([
            dcc.Location(id="url", refresh=False),
            dbc.Container(id="container-main", children=[
                dbc.Row(dbc.Col(get_navbar(title), width=12, className="p-0")),
                dbc.Row(id="row-main"),
                dbc.Button(
                    html.Span(className="fa fa-chevron-right"),
                    id="btn-next", color="secondary", outline=True
                ),
                dbc.Button(
                    html.Span(className="fa fa-chevron-left"),
                    id="btn-prev", color="secondary", outline=True
                )
            ]),
        ])
    return _layout

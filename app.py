"""Function to create dash app"""
from dash import Dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

from src import ASSETS_PATH
from src.callbacks import add_callbacks


def get_navbar() -> dbc.NavbarSimple:
    """Get layout for static navbar"""
    return dbc.NavbarSimple([
        dbc.NavItem(dbc.NavLink("Overview", href="/overview")),
        dbc.DropdownMenu([
            dbc.DropdownMenuItem("Data", href="/data"),
            dbc.DropdownMenuItem("Question 1", href="/question1"),
            dbc.DropdownMenuItem("Question 2", href="/question2"),
            dbc.DropdownMenuItem("Question 3", href="/question3"),
        ], nav=True, in_navbar=True, label="Pages", right=True),
    ], brand="My slideshow title", brand_href="/overview", color="primary", dark=True, sticky="top")


def serve_layout() -> html.Div:
    """Function to create layout on each page refresh"""
    return html.Div([
        dcc.Location(id='url', refresh=False),
        dbc.Container(id="container-main", children=[
            dbc.Row(dbc.Col(get_navbar(), width=12, className="p-0")),
            dbc.Row(id="row-main"),
            dbc.Button(
                html.Span(className="fa fa-chevron-right"),
                id="btn-next", color="secondary", outline=True),
            dbc.Button(
                html.Span(className="fa fa-chevron-left"),
                id="btn-prev", color="secondary", outline=True)
        ]),
    ])


def create_app(debug: bool = True) -> Dash:
    """Create and return dash app"""
    app = Dash(
        __name__,
        assets_folder=ASSETS_PATH,
        suppress_callback_exceptions=True,
        meta_tags=[
            {'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'},
            {'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}
        ],
        external_stylesheets=[
            dbc.themes.BOOTSTRAP,
            "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
        ]
    )
    app.title = 'My Slideshow'
    app.layout = serve_layout
    app.enable_dev_tools(debug=debug)
    add_callbacks(app)
    return app


if __name__ == '__main__':
    debug = True
    app = create_app(debug)
    app.scripts.config.serve_locally = debug
    app.run_server(host='0.0.0.0', debug=debug, port=8050)

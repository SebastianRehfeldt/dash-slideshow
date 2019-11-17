"""Function to create dash app"""
from dash import Dash
import dash_bootstrap_components as dbc

from src import ASSETS_PATH
from src.layout import serve_layout
from src.callbacks import add_callbacks


def create_app(title: str, debug: bool = True) -> Dash:
    """Create and return dash app"""
    app = Dash(
        __name__,
        assets_folder=ASSETS_PATH,
        suppress_callback_exceptions=True,
        meta_tags=[
            {"http-equiv": "X-UA-Compatible", "content": "IE=edge"},
            {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
        ],
        external_stylesheets=[
            dbc.themes.BOOTSTRAP,
            "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
        ]
    )
    app.title = title
    app.layout = serve_layout(title)
    app.enable_dev_tools(debug=debug)
    add_callbacks(app)
    return app

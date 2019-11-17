"""Module for creating plots"""
import pandas as pd
import dash_core_components as dcc
import plotly.graph_objects as go


def create_histogram(df: pd.DataFrame, column: str) -> dcc.Graph:
    """Create Histogram for dataframe and column"""
    return dcc.Graph(
        id="graph-{:s}".format(column),
        figure={
            "data": [go.Histogram(x=df[column])],
            "layout": {
                "title": column.title(),
                "xaxis": {"title": column.title()},
                "yaxis": {"title": "Frequency"},
            }
        }
    )

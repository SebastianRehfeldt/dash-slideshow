"""Module for creating plots"""
from typing import List
import pandas as pd
import dash_core_components as dcc
import plotly.graph_objects as go


def create_histogram(df: pd.DataFrame, column: str) -> dcc.Graph:
    """Create Histogram for dataframe and column"""
    return dcc.Graph(
        id='graph-{:s}'.format(column),
        figure={
            'data': [go.Histogram(x=df[column])],
            'layout': {
                'title': column.title(),
                "xaxis": {'title': column.title()},
                "yaxis": {'title': "Frequency"},
            }
        }
    )


def create_scatter(df: pd.DataFrame, remark: str, columns: List[str]) -> dcc.Graph:
    """Create scatterplot for dataframe and columns"""
    return dcc.Graph(
        id='graph-{:s}'.format(columns[0]),
        figure={
            'data': [go.Scattergl(x=df[columns[0]], y=df[columns[1]], mode="markers")],
            'layout': {
                'title': "{:s} vs. {:s} ({:s})".format(*columns, remark),
                "xaxis": {'title': columns[0]},
                "yaxis": {'title': columns[1]},
            },
        }
    )


def create_grouped_scatter(df: pd.DataFrame, airports: List[str], remark: str) -> dcc.Graph:
    """Create grouped scatterplot for dataframe and columns"""
    columns = ["delay_arrival", "delay_departure"]
    return dcc.Graph(
        id='graph-{:s}'.format(remark),
        figure={
            'data': [
                go.Scattergl(x=df.loc[df["origin"] == i, columns[0]],
                             y=df.loc[df["origin"] == i, columns[1]],
                             mode="markers", name=i)
                for i in airports
            ],
            'layout': {
                'title': remark,
                "xaxis": {'title': columns[0]},
                "yaxis": {'title': columns[1]},
            },
        }
    )


def create_grouped_boxplot(df: pd.DataFrame, airports: List[str], column: str, use_log: bool = False) -> dcc.Graph:
    """Create grouped scatterplot for dataframe and columns"""
    yaxis = {"type": "log"} if use_log else {}
    return dcc.Graph(
        id='graph-{:s}'.format(column),
        figure={
            'data': [
                go.Box(y=df.loc[df["origin"] == i, column],
                       name=i, boxpoints=False)
                for i in airports
            ],
            'layout': {
                'title': column.title(),
                "yaxis": yaxis
            },
        }
    )


def create_boxplot(df: pd.DataFrame, column: str) -> dcc.Graph:
    """Create Histogram for dataframe and column"""
    return dcc.Graph(
        id='graph-{:s}'.format(column),
        figure={
            'data': [go.Box(y=df[column])],
            'layout': {
                'title': column.title()
            },
        }
    )

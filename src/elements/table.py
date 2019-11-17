"""Dash datatable helper function"""
import pandas as pd
from dash_table.DataTable import DataTable


def create_table(df: pd.DataFrame, label: str) -> DataTable:
    """Create a data table"""
    return DataTable(
        id="table-{:s}".format(label),
        columns=[{"name": i.title(), "id": i} for i in df.columns],
        data=df.to_dict("records"),
        style_cell_conditional=[
            {"if": {"column_id": c}, "textAlign": "center"}
            for c in ["A", "B", "C"]
        ],
        style_data_conditional=[{
            "if": {"row_index": "odd"},
            "backgroundColor": "rgb(248, 248, 248)"
        }],
        style_header={
            "backgroundColor": "white",
            "fontWeight": "bold"
        },
        sort_action="native",
        filter_action="native",
        page_action="native",
        page_size=16,
        style_table={"overflowX": "auto", "overflowY": "auto"},
    )

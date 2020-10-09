# -*- coding: utf-8 -*-

# Script with common functions

import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

def import_style(filename):
    """
    Import a custom CSS style
    Parameters:
        filename (str): stylesheet to import
    Return:
        style (html.Link): imported stylesheet
    """

    style = html.Link(
        href=filename,
        rel='stylesheet'
    )
    return style


def get_trigger_id():
    """
    Get the id of the element that trigger a callback
    Return:
        id (str): id of the element
    """

    ctx = dash.callback_context
    id = ctx.triggered[0]['prop_id'].split('.')[0]
    return id


def generate_table(dataframe, max_rows=0):
    """
    Generate a table from a DataFrame
    Parameters:
        dataframe (DataFrame): data to read
        max_rows (int): maximum number of rows to read from data. default = 0 (show all rows in dataframe)
    Return:
        table (Bootstrap table): generated table
    """

    # print('  *** generate_table()')
    table_header = [
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns]))
    ]

    rows = []
    if(max_rows == 0):
        max_rows = len(dataframe)
    for i in range(min(len(dataframe), max_rows)):
        rows.append(
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ])
        )
    table_body = [html.Tbody(rows)]
    table = dbc.Table(table_header + table_body, bordered=True)
    
    return table


def read_csv(filename):
    """
    Read a CSV as a DataFrame
    Parameters:
        filename (str): file to read
    Return:
        data (DataFrame): file data
    """

    # print('  *** read_csv()')
    data = pd.read_csv(filename)

    return data

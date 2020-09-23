# -*- coding: utf-8 -*-

# Script of the Classification page

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

import config
import common
from navbar import Navbar

nav = Navbar()
style = common.import_style(config.custom_style)
body = dbc.Container(children=[
    style,
    html.H1(children='Stage 2 - Variant classification'),
], className="mt-1",)

def Classification():
    layout = html.Div([
    nav,
    style,
    html.Br(),
    html.Br(),
    body
    ])
    return layout

app = dash.Dash(
    __name__, 
    external_stylesheets = [dbc.themes.UNITED]
    # external_stylesheets=external_stylesheets
)
app.layout = Classification()

# -*- coding: utf-8 -*-

# Script of the Training page

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import config
import common
from navbar import Navbar

expertise_level = ['Novice', 'Advanced Beginner', 'Competent', 'Proficient', 'Expert']
labels = ['Benign', 'Likely Benign', 'VUS', 'Likely Pathogenic', 'Pathogenic']
acmg_rules = "/static/ACMG_rules.jpg"

nav = Navbar()
style = common.import_style(config.custom_style)
modal = html.Div(
    [
        dbc.Button("Need to remember ACMG rules?", id="open", outline=True),
        dbc.Modal(
            [
                dbc.ModalHeader("ACMG rules"),
                # dbc.ModalBody("This is the content of the modal"),
                dbc.ModalBody(
                    html.Div([
                        html.Img(src=acmg_rules)
                        ], className="image"),
                    ),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close", className="ml-auto")
                ),
            ],
            id="modal",
            size='xl',
        ),
    ]
)

body = dbc.Container(children=[
    html.H1(children='Stage 1 - Variant classification and expert training'),

    html.P("What do you consider to be your level of expertise in the interpretation of variants?:"),
    html.Div(
        # className='five columns',
        children=[
            dcc.Dropdown(
                id='combo-levels',
                options=[{'label': i, 'value': i} for i in expertise_level],
                value=''
            )
        ]
    ),
    html.Hr(),
    html.Br(),
    dbc.Button(children='Load new variant', id='btn-load-new-variant-2', n_clicks=0, color='primary'),
    # dbc.Button("Primary", color="primary", className="mr-1"),
    html.Br(),
    html.Br(),
    html.Div(id='loaded-variant', children=''),
    html.Br(),
    
    html.P(children='According to the information provided above, the classification of the variant corresponds to:'),
    html.Div(
        # className='five columns',
        children=[
            dcc.Dropdown(
                id='combo-labels',
                options=[{'label': i, 'value': i} for i in labels],
                value=''
            ),
            html.Br(),
            dbc.Alert(id='msg', children='', color='danger'),
        ]
    ),
    modal,
], className="mt-1",)


def Training():
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
app.layout = Training()

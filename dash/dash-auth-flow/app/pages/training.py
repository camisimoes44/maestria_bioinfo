import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from dash import no_update
import random
from flask_login import current_user
import time
from functools import wraps
import pandas as pd
from dash.exceptions import PreventUpdate
# import MySQLdb
import requests

from server import app

login_alert = dbc.Alert(
    'User not logged in. Taking you to login.',
    color='danger'
)

location = dcc.Location(id='page1-url', refresh=True)
expertise_level = ['Novice', 'Advanced Beginner', 'Competent', 'Proficient', 'Expert']
labels = ['Benign', 'Likely Benign', 'VUS', 'Likely Pathogenic', 'Pathogenic']
input_csv = "static/genomic.csv"
expected_label = ''
df = pd.read_csv(input_csv)


def layout():
    # if current_user.is_authenticated:
    return dbc.Row(
        dbc.Col(
            [
                location,
                html.Div(id='page1-login-trigger'),

                html.H1('Stage 1 - Variant classification and expert training'),
                html.Br(),
                # dbc.Row(children=[
                #     dbc.Col([
                #         html.P("What do you consider to be your level of expertise in the interpretation of variants?:"),
                #         html.Div(
                #             # className='five columns',
                #             children=[
                #                 dcc.Dropdown(
                #                     id='combo-levels',
                #                     options=[{'label': i, 'value': i} for i in expertise_level],
                #                     value=''
                #                 )
                #             ]
                #         ),
                #     ], width=3),
                #     dbc.Col([
                #         html.P("What do you consider to be your level of expertise in the interpretation of variants?:"),
                #         html.Div(
                #             # className='five columns',
                #             children=[
                #                 dcc.Dropdown(
                #                     id='combo-lev',
                #                     options=[{'label': i, 'value': i} for i in expertise_level],
                #                     value=''
                #                 )
                #             ]
                #         ),
                #     ], width=3),
                # ]),

                html.Div(id='page1-test-trigger'),
                # dcc.Loading(html.Iframe(id='page1-test',style=dict(height='500px',width='100%')),id='page1-loading')

                dbc.Button(children='Load new variant', id='btn-load-new-variant-2', n_clicks=0, color='primary'),
                # dbc.Button("Primary", color="primary", className="mr-1"),
                html.Br(),
                html.Br(),
                html.Div(id='loaded-variant', children=''),
                html.Br(),

                html.P(
                    children='According to the information provided above, the classification of the variant '
                             'corresponds to:'),
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

                dbc.Button(children='Read from DB', id='btn-load-db', n_clicks=0, color='primary'),
                html.Br(),
                html.P('Data from DB'),
                html.Div(id='loaded-data-db', children=''),
                html.Br(),

            ], width=12)
    )


# @app.callback(
#     Output('page1-test','src'),
#     [Input('page1-test-trigger','children')]
# )
# def page1_test_update(trigger):
#     '''
#     updates iframe with example.com
#     '''
#     time.sleep(2)
#     return 'http://example.com/'

@app.callback(
    Output('loaded-data-db', 'children'),
    [(Input('btn-load-db', 'n_clicks'))]
)
def read_from_db(n_clicks):
    if n_clicks != 0:
        api_url = 'http://127.0.0.1:5000/listado'
        response = requests.post(api_url)
        # print(response)
        if response.status_code == 200:
            # return json.loads(response.content.decode('utf-8'))
            data_df = pd.read_json(response.content.decode('utf-8'))
            table = dbc.Table.from_dataframe(data_df, striped=True, bordered=True, hover=True)
            return table
        else:
            return 'None'
    else:
        raise PreventUpdate


@app.callback(
    Output('loaded-variant', 'children'),
    [Input('btn-load-new-variant-2', 'n_clicks')]
)
def update_loaded_variant(n_clicks):
    """
    Update the loaded variants as a table
    Return:
        table (Bootstrap table): loaded variants
    """

    # print(common.get_trigger_id())

    if n_clicks != 0:
        loaded_variant = load_new_variant()
        # print(n_clicks, type(loaded_variant), loaded_variant.Start)
        global expected_label
        expected_label = loaded_variant.TUTEDX_ACMG.values[0]
        # print('expected_label:', expected_label, type(expected_label))
        data = [loaded_variant.Start, loaded_variant.Ref, loaded_variant.Alt, loaded_variant.ExonicFunc,
                loaded_variant.Exome_flag, loaded_variant.TUTEDX_ACMG]
        data_show = pd.concat(data, axis=1, keys=['Start', 'Ref', 'Alt', 'ExonicFunc', 'Exome_flag', 'TUTEDX_ACMG'])
        # return common.generate_table(data_show)
        table = dbc.Table.from_dataframe(data_show, striped=True, bordered=True, hover=True)
        return table
    else:
        raise PreventUpdate  # no actualizar la tabla


def load_new_variant():
    """
    Load a random variant from the CSV
    Return:
        data_s (DataFrame): loaded data
    """

    # print('  *** load_new_variant()')
    data_s = df.sample()

    return data_s

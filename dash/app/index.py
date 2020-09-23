# -*- coding: utf-8 -*-

# Main script of the system

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import pandas as pd

import config
import common

# import script of pages
from login import Login
from training import Training
from classification import Classification
from homepage import Homepage


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
    )
app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
    ])  # space where we return the pages
server = app.server  # to allow run in production mode


# callback to display pages based on the current URL
@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '' or pathname == '/' or pathname == config.login_url:
        # print('--> login')
        return Login()
    elif pathname == config.home_url:
        # print('--> home')
        return Homepage()
    elif pathname == config.training_url:
        # print('--> training')
        return Training()
    elif pathname == config.classification_url:
        # print('--> classification')
        return Classification()


# home page ###############################################################################


# login page ##############################################################################


# training page ###########################################################################

input_csv = "static/genomic.csv"
expected_label = ''
df = common.read_csv(input_csv)

def loadNewVariant():
    """
    Load a random variant from the CSV
    Return:
        data_s (DataFrame): loaded data
    """

    # print('  *** loadNewVariant()')
    data_s = df.sample()
    
    return data_s


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

    print(common.get_trigger_id())

    if n_clicks != 0:
        loaded_variant = loadNewVariant()
        # print(n_clicks, type(loaded_variant), loaded_variant.Start)
        global expected_label
        expected_label = loaded_variant.TUTEDX_ACMG.values[0]
        # print('expected_label:', expected_label, type(expected_label))
        data = [loaded_variant.Start, loaded_variant.Ref, loaded_variant.Alt, loaded_variant.ExonicFunc, loaded_variant.Exome_flag, loaded_variant.TUTEDX_ACMG]
        data_show = pd.concat(data, axis=1, keys=['Start', 'Ref', 'Alt', 'ExonicFunc', 'Exome_flag', 'TUTEDX_ACMG'])
        # return common.generate_table(data_show)
        table = dbc.Table.from_dataframe(data_show, striped=True, bordered=True, hover=True)
        return table
    else:
        raise PreventUpdate  # no actualizar la tabla


@app.callback(
    [Output('msg', 'children'),
    Output('msg', 'color')],
    [Input('combo-labels', 'value')]
    )
def update_msg(value):
    """
    Update the message after the user select a label
    Parameter:
        value (str): label selected by the user
    Return:
        msg (str): message to show to the user
        color (str): CSS class to set to the message
    """
    
    print(common.get_trigger_id())
    # print('***' + value + '*** ***' + expected_label + '***')

    if(value != '' and expected_label != ''):
        if (value == expected_label):
            msg = "Well done!"
            color = "success"
        else:
            msg = "The expected label was: " + expected_label
            color = "danger"
        return msg, color
    else:
        # raise PreventUpdate
        return '', ''


@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    """
    Show/hide the modal window
    """
    if n1 or n2:
        return not is_open
    return is_open


# classification page #####################################################################


if __name__ == '__main__':
    app.run_server(
        debug=config.debug,
        port=config.port,
        host=config.host
    )
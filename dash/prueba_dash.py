# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 13:27:30 2020

@author: Camila
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Are you a cat person?'),
    html.Label('Your name: '),
    dcc.Input(id='input-div'),
    html.Div(id='output-div', children=[])
])

@app.callback(
        Output(component_id='output-div', component_property='children'),
        [Input(component_id='input-div', component_property='value')]
)
def update_output(input_value):
    if input_value is None or not input_value:
        return ['You have not typed your name yet.']
    if input_value == 'Heisenberg':
        return ['You are a cat person.']
    else:
        return ['You are a dog person.']

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8888, debug=True)
# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('example_4', external_stylesheets=external_stylesheets)

ratio = 0.1

reference = {
    'name': 'Simple Interactive Dash App',
    'url': 'https://dash.plotly.com/basic-callbacks'
}

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div(["Input: ",
              dcc.Input(id="my-input", value="inital-value", type="text")]),
    html.Br(),
    html.Div(id="my-output")
])

@app.callback(
    dash.dependencies.Output(component_id='my-output', component_property='children'),
    [dash.dependencies.Input(component_id='my-input', component_property='value')]
)
def update_output_div(input_value):
    return f'Output {input_value}'
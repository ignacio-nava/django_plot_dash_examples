# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('example_2', external_stylesheets=external_stylesheets)

ratio = 0.4

reference = {
    'name': 'Dash Layout',
    'url': 'https://dash.plotly.com/layout'
}


df = pd.DataFrame({
    'Fruit': ['Apples', 'Banana', 'Orange'],
    'Amount': [4,1,3],
    'City': ['SF', 'NY', 'Montreal']
})

fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

app.layout = html.Div(
    children=[
        html.H1(
            children="Hello Dash"
            ),

        html.Div(
            children='''Dash: A web application framework for Python.'''
        ),

        dcc.Graph(
            id="example-figure",
            figure=fig
        )
    ]
)

# app.layout = html.Div(
#     children=[
#         html.H1(children='Hello Dash'),
#         html.Div(children=
#             '''Dash: a web application framework for Python'''
#         ),
#         dcc.Graph(
#             id='example-graph',
#             figure=fig
#         )
#     ]
# )

# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from pandas_datareader import data as web
from datetime import datetime as dt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv'
    )

app.layout = html.Div(children=[
    html.H1(
        children=('Precio acción'),style={'textAlign': 'center'}
    ),
    html.Div(children='Gráficas en python.', style={'textAlign': 'center'}
    ),

    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coca-cola', 'value': 'COKE'},
            {'label': 'Tesla', 'value': 'TSLA'},
            {'label': 'Apple', 'value': 'AAPL'}
        ],
        value = 'COKE'
    ),

    html.Div(id="output-container"),

    dcc.Graph(id='my-graph'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ['Máximo Acción', 'Mínimo Acción'], 'y': [211.28, 126.80], 'type': 'bar', 'name': 'Coca-cola'},
                {'x': ['Máximo Acción', 'Mínimo Acción'], 'y': [379.57, 250,56], 'type': 'bar', 'name': u'Tesla'},
                {'x': ['Máximo Acción', 'Mínimo Acción'], 'y': [229.28, 155.15], 'type': 'bar', 'name': 'Apple'},
            ]
        }
    ),
    
    html.H1(
        children=('Esperanza de vida'),style={'textAlign': 'center'}
    ),

    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

@app.callback(
    dash.dependencies.Output('output-container', 'children'),
    [dash.dependencies.Input('my-dropdown', 'value')])
def update_output(value):
    return 'Has seleccionado: "{}"'.format(value)

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    df = web.DataReader(
       selected_dropdown_value, data_source='yahoo',
       start=dt(2018, 1, 1), end=dt.now())

    return {
        'data': [{
            'x': df.index,
            'y': df.Close
        }]
    }
if __name__ == '__main__':
    app.run_server(host="0.0.0.0",debug=True)
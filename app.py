# Import required libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import pathlib
import pandas as pd
import plotly.express as px

import os
import flask

server = flask(__name__)
app = dash.dash(__name__, server = server)


# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()
df1 = px.data.gapminder().query("year == 2007")

# Load data
df = pd.read_csv(DATA_PATH.joinpath("10012776-biblioteca.csv"), sep=';', low_memory=False)
df['Data hora'] = pd.to_datetime(df['Data hora'])
df['Activa kW'] = df['Activa kW'].astype(float)
df['Reactiva Indutiva kVAR'] = df['Reactiva Indutiva kVAR'].astype(float)
df['Reactiva Capacitiva kVAR'] = df['Reactiva Capacitiva kVAR'].astype(float)

lares = [['Centro Social e Paroquial de Cabril', 41.714849, -8.034901, 30, 580283.49, 4618566.98, 8172.777, 227274.399],
         ['Centro Social e Paroquial de Vilar de Perdizes', 41.855523, -7.633986, 10, 613386.77, 4634637.30, 41446.133,243014.733],
         ['Lar Monte Sereno', 41.798622, -7.666606, 37, 610777.14, 4628277.08, 38771.743,236679.488],
         ['Lar Nossa Senhora do Pranto',41.641292, -7.945080,30, 587855.50,4610487.98, 15665.477,219117.06],
         ['Lar dos Pisões para Seniores', 41.737331, -7.869785, 22, 593986.37,4621230.21, 21906.038,229800.279],
         ['Santa Casa da Misericórdia - Lar', 41.822516, -7.790499, 80,600446.70,4630777.71, 28464.204,239284.931],
         ['Residencial Santa Clara', 41.785061, -7.781880, 36,601221.45, 4626629.28, 29180.277, 239287.822]]
         
    
# Create the pandas DataFrame
df1 = pd.DataFrame(lares, columns = ['Name', 'lat', 'long', 'pop', 'UTM_Easting', 'UTM_Northing', 'x_ETRS89','y_ETRS89'])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'CHANGE'
            }
        }
    ),

    
    dcc.Graph(
    id='example-graph3',
    figure = px.line(df, x='Data hora', y='Activa kW')),

    dcc.Graph(
    id='example-graph4',
    figure = px.scatter_mapbox(df1, lat="lat", lon="long",
                            color_discrete_sequence=["fuchsia"], zoom=100, height=600,mapbox_style="open-street-map"))
                            
])


if __name__ == '__main__':
    app.run_server(debug=True)
    
    

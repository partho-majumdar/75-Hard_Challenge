import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("./gapminder.csv")

app = dash.Dash()

# app.layout = html.H1(children="My first dashboard", style={'color': 'red', 'text-align': 'center'})

app.layout = html.Div(
    [
        html.Div(
            children=[
                html.H2("My first div", style={"color": "red", "text-align": "center"})
            ],
            style={
                "border": "1px solid red",
                "float": "left",
                "width": "100%",
                "height": "50px",
            },
        ),
        html.Div(
            style={
                "border": "1px solid red",
                "float": "left",
                "width": "49.5%",
                "height": "350px",
            }
        ),
        html.Div(
            style={
                "border": "1px solid red",
                "float": "left",
                "width": "49.5%",
                "height": "350px",
            }
        ),
    ]
)


app.layout = html.Div(
    [
        html.Div(
            children=[
                html.H2("My first div", style={"color": "red", "text-align": "center"})
            ],
            style={
                "border": "1px solid red",
                "float": "left",
                "width": "100%",
                "height": "50px",
            },
        ),
        html.Div(
            children=[
                dcc.Graph(
                    id="scatter-plot",
                    figure={
                        "data": [
                            go.Scatter(
                                x=data["pop"], y=data["gdpPercap"], mode="markers"
                            )
                        ],
                        "layout": go.Layout(title="Scatter Plot"),
                    },
                )
            ],
            style={
                "border": "1px solid red",
                "float": "left",
                "width": "49.5%",
                # "height": "350px",
            },
        ),
        html.Div(
            children=[
                dcc.Graph(
                    id="box-plot",
                    figure={
                        "data": [go.Box(x=data["gdpPercap"])],
                        "layout": go.Layout(title="Box plot"),
                    },
                )
            ],
            style={
                "border": "1px solid red",
                "float": "left",
                "width": "49.5%",
                # "height": "350px",
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

import dash
import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

patients = pd.read_csv("./IndividualDetails.csv")
total = patients.shape[0]
hospitalized = patients[patients["current_status"] == "Hospitalized"].shape[0]
recovered = patients[patients["current_status"] == "Recovered"].shape[0]
deaths = patients[patients["current_status"] == "Deceased"].shape[0]

options = [
    {"label": "All", "value": "All"},
    {"label": "Hospitalized", "value": "Hospitalized"},
    {"label": "Recovered", "value": "Recovered"},
    {"label": "Deceased", "value": "Deceased"},
]

# app.layout=html.H1("This is h1 inside layout")
app.layout = html.Div(
    [
        html.H1(
            "Corona virus pandemic",
            style={
                "color": "#fff",
                "text-align": "center",
                "padding": "10px",
            },
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H3("Total Cases", className="card-title"),
                                        html.H4(total, className="card-text"),
                                    ],
                                    className="card-body",
                                )
                            ],
                            className="card text-white bg-primary mb-3",
                            style={"maxWidth": "18rem"},
                        )
                    ],
                    className="col-md-3",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H3("Recovered", className="card-title"),
                                        html.H4(recovered, className="card-text"),
                                    ],
                                    className="card-body",
                                )
                            ],
                            className="card text-white bg-success mb-3",
                            style={"maxWidth": "18rem"},
                        )
                    ],
                    className="col-md-3",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H3("Deaths", className="card-title"),
                                        html.H4(deaths, className="card-text"),
                                    ],
                                    className="card-body",
                                )
                            ],
                            className="card text-white bg-danger mb-3",
                            style={"maxWidth": "18rem"},
                        )
                    ],
                    className="col-md-3",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        html.H3("Active Cases", className="card-title"),
                                        html.H4(hospitalized, className="card-text"),
                                    ],
                                    className="card-body",
                                )
                            ],
                            className="card text-white bg-warning mb-3",
                            style={"maxWidth": "18rem"},
                        )
                    ],
                    className="col-md-3",
                ),
            ],
            className="row",
        ),
        html.Div([], className="row"),
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [
                                        dcc.Dropdown(
                                            id="picker", options=options, value="All"
                                        ),
                                        dcc.Graph(id="bar"),
                                    ],
                                    className="card-body",
                                )
                            ],
                            className="card",
                        )
                    ],
                    className="col-md-12",
                )
            ],
            className="row",
        ),
    ],
    className="container",
)


@app.callback(Output("bar", "figure"), [Input("picker", "value")])
def update_graph(type):

    if type == "All":
        patients_bar = patients["detected_state"].value_counts().reset_index()
        return {
            "data": [go.Bar(x=patients_bar["detected_state"], y=patients_bar["count"])],
            "layout": go.Layout(title="State total count"),
        }
    else:
        n_patients = patients[patients["current_status"] == type]
        patients_bar = n_patients["detected_state"].value_counts().reset_index()
        return {
            "data": [go.Bar(x=patients_bar["detected_state"], y=patients_bar["count"])],
            "layout": go.Layout(title="State total count"),
        }


if __name__ == "__main__":
    app.run_server(debug=True)


"""
div -> split entire container into 12 equal parts
"""

# Necessary imports - do not change, and include on every slide
from dash import html, dcc
from app import app
import dash_bootstrap_components as dbc

###

content = html.Div(
    style={"textAlign": "center"},
    children=[
        dbc.Card(
            style={"backgroundColor": "#e8f4ff", "marginTop": "6rem"},
            children=[
                dbc.CardBody(
                    [
                        html.Div([html.H4("Introduction")], className="py-2"),

                        html.Div(
                            style={"textAlign": "left", "fontSize": 17},
                            children=[
                                html.P(
                                    "This presentation is a real-case example based on actual cement plant quality "
                                    "characteristics.",
                                    className="lead",
                                ),
                                html.P(
                                    "It demonstrates the key parameters that must be controlled during cement production "
                                    "across different cement types and production plants."
                                ),
                                html.P(
                                    "The application utilizes fundamental cement characteristics to predict the 2-day "
                                    "compressive strength, illustrating a practical approach to cement quality control."
                                ),
                                dbc.Alert(
                                    "In addition, it introduces basic statistical analysis methods used to evaluate "
                                    "process stability and performance.",
                                    color="info",
                                    className="mt-3 mb-0",
                                ),
                            ],
                        ),
                    ]
                )
            ],
            className="shadow-lg p-3 rounded",
        )
    ],
)

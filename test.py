import sqlalchemy as sa
from sqlalchemy.schema import MetaData
import pandas as pd


engine = sa.create_engine("sqlite:///sqlalchemyCFTCDATA.sqlite")
df = pd.read_sql("EUR", engine)
df.Date = pd.to_datetime(df.Date)

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import plotly.express as px

# the style arguments for the sidebar.
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20%",
    "padding": "20px 10px",
    "background-color": "#f8f9fa",
}

# the style arguments for the main content page.
CONTENT_STYLE = {"margin-left": "25%", "margin-right": "5%", "padding": "20px 10p"}

TEXT_STYLE = {"textAlign": "center", "color": "#191970"}

CARD_TEXT_STYLE = {"textAlign": "center", "color": "#0074D9"}

sidebar = html.Div(
    [html.H2("Menu", style=TEXT_STYLE), html.Hr()],
    style=SIDEBAR_STYLE,
)

content_first_row = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4(
                                id="card_title_1",
                                children=["Last:"],
                                className="card-title",
                                style=CARD_TEXT_STYLE,
                            ),
                            html.P(
                                id="card_text_1",
                                children=["Sample text."],
                                style=CARD_TEXT_STYLE,
                            ),
                        ]
                    )
                ]
            ),
            md=3,
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4(
                                id="Card Title 2",
                                children=["Average:"],
                                className="card-title",
                                style=CARD_TEXT_STYLE,
                            ),
                            html.P("Sample text.", style=CARD_TEXT_STYLE),
                        ]
                    ),
                ]
            ),
            md=3,
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4(
                                id="Card Title 3",
                                children=["High:"],
                                className="card-title",
                                style=CARD_TEXT_STYLE,
                            ),
                            html.P("Sample text.", style=CARD_TEXT_STYLE),
                        ]
                    ),
                ]
            ),
            md=3,
        ),
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H4(
                                id="Card Title 4",
                                children=["Low:"],
                                className="card-title",
                                style=CARD_TEXT_STYLE,
                            ),
                            html.P("Sample text.", style=CARD_TEXT_STYLE),
                        ]
                    ),
                ]
            ),
            md=3,
        ),
    ]
)

content_second_row = dbc.Row(
    [
        dbc.Col(dcc.Graph(id="graph_1"), md=4),
        dbc.Col(dcc.Graph(id="graph_2"), md=4),
        dbc.Col(dcc.Graph(id="graph_3"), md=4),
    ]
)

content_third_row = dbc.Row(
    [
        dbc.Col(
            dcc.Graph(id="graph_4"),
            md=12,
        )
    ]
)

content_fourth_row = dbc.Row(
    [dbc.Col(dcc.Graph(id="graph_5"), md=6), dbc.Col(dcc.Graph(id="graph_6"), md=6)]
)

content = html.Div(
    [
        html.H2("Analytics Dashboard Template", style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        content_second_row,
        content_third_row,
        content_fourth_row,
    ],
    style=CONTENT_STYLE,
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div([sidebar, content])

if __name__ == "__main__":
    app.run_server(port="8085")

from dash import Dash, html, dcc, Input, Output
from pandas import to_datetime, read_sql
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from plotly.express import line
from listCreations import columnOptions, tableOptions, engine

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
CONTENT_STYLE = {
    "margin-left": "25%",
    "margin-right": "5%",
    "padding": "20px 10p",
}

TEXT_STYLE = {
    "textAlign": "center",
    "color": "#191970",
}

CARD_TEXT_STYLE = {
    "textAlign": "center",
    "color": "#0074D9",
}

sidebar = html.Div(
    [
        html.H2("Menu", style=TEXT_STYLE),
        html.Hr(),
    ],
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
                                id="last",
                                children=[""],
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
                            html.P(
                                id="average",
                                children=[],
                                style=CARD_TEXT_STYLE,
                            ),
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
                            html.P(
                                id="high",
                                children=[],
                                style=CARD_TEXT_STYLE,
                            ),
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
                            html.P(
                                id="low",
                                children=[],
                                style=CARD_TEXT_STYLE,
                            ),
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
            children=[
                dcc.Dropdown(
                    options=columnOptions, value="OpenInterest", id="columnDropdown"
                ),
                dcc.Dropdown(options=tableOptions, value="EUR", id="tableDropdown"),
                dcc.Graph(id="renderedGraph"),
            ],
            md=12,
        )
    ]
)

content_fourth_row = dbc.Row(
    [
        dbc.Col(dcc.Graph(id="graph_5"), md=6),
        dbc.Col(dcc.Graph(id="graph_6"), md=6),
    ]
)

content = html.Div(
    [
        html.H2("Sixteen Analytics Dashboard", style=TEXT_STYLE),
        html.Hr(),
        content_first_row,
        # content_second_row,
        content_third_row,
        content_fourth_row,
    ],
    style=CONTENT_STYLE,
)

app = Dash(
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
    ]
)
load_figure_template("BOOTSTRAP")

app.layout = html.Div(
    [
        sidebar,
        content,
    ]
)


@app.callback(
    Output(component_id="renderedGraph", component_property="figure"),
    Output(component_id="last", component_property="children"),
    Output(component_id="average", component_property="children"),
    Output(component_id="high", component_property="children"),
    Output(component_id="low", component_property="children"),
    Input(component_id="columnDropdown", component_property="value"),
    Input(component_id="tableDropdown", component_property="value"),
)
def renderGraph(selectedColumn, selectedTable):
    df = read_sql(selectedTable, engine)
    df.Date = to_datetime(df.Date)
    lineFig = line(df, x=df.Date, y=selectedColumn, title=f"{selectedColumn}")
    return (
        lineFig,
        int(df[selectedColumn].iloc[0]),
        int(df[selectedColumn].mean()),
        int(df[selectedColumn].max()),
        int(df[selectedColumn].min()),
    )


if __name__ == "__main__":
    app.run_server(port="8085", debug=True)

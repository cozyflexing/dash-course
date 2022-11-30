from dash import Dash, html, dcc, Input, Output
from pandas import to_datetime, read_sql
import pandas as pd
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from plotly.express import line
import plotly.express as px
from listCreations import columnOptions, tableOptions, engine, pie_options

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
    "margin-top": "10px",
    "margin-left": "25%",
    "margin-right": "5%",
    "padding": "20px 10p",
}

TEXT_STYLE = {
    "textAlign": "center",
    "color": "black",
}

CARD_TEXT_STYLE = {
    "textAlign": "center",
    "color": "#black",
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
                                children=["Mean:"],
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
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.Div(
                                [
                                    html.H4("Analysis of positions"),
                                    dcc.Graph(id="pie_chart"),
                                    html.P("Names:"),
                                    dcc.Dropdown(
                                        id="tables",
                                        options=tableOptions,
                                        value="EUR",
                                        clearable=False,
                                    ),
                                    html.P("Values:"),
                                    dcc.Dropdown(
                                        id="category",
                                        options=pie_options,
                                        value="Commercial",
                                        clearable=False,
                                    ),
                                ]
                            )
                        ]
                    ),
                ]
            ),
            md=6,
        ),
    ],
    style=CARD_TEXT_STYLE,
)

content_third_row = dbc.Row(
    [
        dbc.Col(
            children=[
                dcc.Graph(id="rendelightcyanGraph"),
                html.P("Select data type:"),
                dcc.Dropdown(
                    options=columnOptions, value="OpenInterest", id="columnDropdown"
                ),
                html.P(""),
                html.P("Select asset:"),
                dcc.Dropdown(options=tableOptions, value="EUR", id="tableDropdown"),
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
        content_second_row,
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
    Output("pie_chart", "figure"),
    Input("tables", "value"),
    Input("category", "value"),
)
def generate_chart(tables, category):
    df = read_sql(tables, engine)
    df = df.iloc[0]
    if category == "Commercial":
        df = pd.DataFrame(
            [
                [
                    "Short % Commercial",
                    (
                        (df.CommercialShort / (df.CommercialLong + df.CommercialShort))
                        * 100
                    ),
                ],
                [
                    "Long % Commercial",
                    (
                        (df.CommercialLong / (df.CommercialLong + df.CommercialShort))
                        * 100
                    ),
                ],
            ],
            columns=["type", "result"],
        )
        pieChart = px.pie(
            df,
            values="result",
            names="type",
            hole=0.7,
            color_discrete_sequence=["red", "green"],
        )
    if category == "Noncommercial":
        df = pd.DataFrame(
            [
                [
                    "Short % Noncommercial",
                    (
                        (
                            df.NoncommercialShort
                            / (df.NoncommercialLong + df.NoncommercialShort)
                        )
                        * 100
                    ),
                ],
                [
                    "Long % Noncommercial",
                    (
                        (
                            df.NoncommercialLong
                            / (df.NoncommercialLong + df.NoncommercialShort)
                        )
                        * 100
                    ),
                ],
            ],
            columns=["type", "result"],
        )
        pieChart = px.pie(
            df,
            values="result",
            names="type",
            hole=0.7,
            color_discrete_sequence=["red", "green"],
        )
    if category == "Nonreportable Positions":
        df = pd.DataFrame(
            [
                [
                    "Short % Nonreportable Positions",
                    (
                        (
                            df.NonreportablePositionsShort
                            / (
                                df.NonreportablePositionsLong
                                + df.NonreportablePositionsShort
                            )
                        )
                        * 100
                    ),
                ],
                [
                    "Long % Nonreportable Positions",
                    (
                        (
                            df.NonreportablePositionsLong
                            / (
                                df.NonreportablePositionsLong
                                + df.NonreportablePositionsShort
                            )
                        )
                        * 100
                    ),
                ],
            ],
            columns=["type", "result"],
        )
        pieChart = px.pie(
            df,
            values="result",
            names="type",
            hole=0.7,
            color_discrete_sequence=["red", "green"],
        )
    pieChart.update(layout_showlegend=False)
    pieChart.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    return pieChart


@app.callback(
    Output(component_id="rendelightcyanGraph", component_property="figure"),
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
    mask = df["Date"] > "2017-01-01"
    df = df.loc[mask]
    lineFig = line(df, x=df.Date, y=selectedColumn, title=f"{selectedColumn}")
    lineFig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all"),
                ]
            )
        ),
    )
    return (
        lineFig,
        int(df[selectedColumn].iloc[0]),
        int(df[selectedColumn].mean()),
        int(df[selectedColumn].max()),
        int(df[selectedColumn].min()),
    )


if __name__ == "__main__":
    app.run_server(port="8085", debug=True)

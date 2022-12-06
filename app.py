from dash import Dash, html, dcc, Input, Output, dash_table
from pandas import to_datetime, read_sql
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from plotly.express import line
import plotly.express as px
from listCreations import columnOptions, tableOptions, engine, pie_options
import functions


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

PIE_CARD_TEXT_STYLE = {
    "textAlign": "center",
    "color": "#black",
}
TABLE_CARD_TEXT_STYLE = {
    "textAlign": "left",
    "color": "#black",
}

PIE_CHART_DIV_STYLE = {
    "position": "relative",
}

sidebar = html.Div(
    [
        html.H2("Menu", style=TEXT_STYLE),
        html.Hr(),
    ],
    style=SIDEBAR_STYLE,
)

# content_first_row = dbc.Row(
#     [
#         dbc.Col(
#             dbc.Card(
#                 [
#                     dbc.CardBody(
#                         [
#                             html.H4(
#                                 id="card_title_1",
#                                 children=["Last:"],
#                                 className="card-title",
#                                 style=PIE_CARD_TEXT_STYLE,
#                             ),
#                             html.P(
#                                 id="last",
#                                 children=[""],
#                                 style=PIE_CARD_TEXT_STYLE,
#                             ),
#                         ]
#                     )
#                 ]
#             ),
#             md=3,
#         ),
#         dbc.Col(
#             dbc.Card(
#                 [
#                     dbc.CardBody(
#                         [
#                             html.H4(
#                                 id="Card Title 2",
#                                 children=["Mean:"],
#                                 className="card-title",
#                                 style=PIE_CARD_TEXT_STYLE,
#                             ),
#                             html.P(
#                                 id="average",
#                                 children=[],
#                                 style=PIE_CARD_TEXT_STYLE,
#                             ),
#                         ]
#                     ),
#                 ]
#             ),
#             md=3,
#         ),
#         dbc.Col(
#             dbc.Card(
#                 [
#                     dbc.CardBody(
#                         [
#                             html.H4(
#                                 id="Card Title 3",
#                                 children=["High:"],
#                                 className="card-title",
#                                 style=PIE_CARD_TEXT_STYLE,
#                             ),
#                             html.P(
#                                 id="high",
#                                 children=[],
#                                 style=PIE_CARD_TEXT_STYLE,
#                             ),
#                         ]
#                     ),
#                 ]
#             ),
#             md=3,
#         ),
#         dbc.Col(
#             dbc.Card(
#                 [
#                     dbc.CardBody(
#                         [
#                             html.H4(
#                                 id="Card Title 4",
#                                 children=["Low:"],
#                                 className="card-title",
#                                 style=PIE_CARD_TEXT_STYLE,
#                             ),
#                             html.P(
#                                 id="low",
#                                 children=[],
#                                 style=PIE_CARD_TEXT_STYLE,
#                             ),
#                         ]
#                     ),
#                 ]
#             ),
#             md=3,
#         ),
#     ]
# )

content_second_row = dbc.Row(
    [
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.Div(
                                [
                                    dcc.Graph(id="pie_chart"),
                                ],
                                style=PIE_CHART_DIV_STYLE,
                            ),
                        ]
                    ),
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
            ),
            style=PIE_CARD_TEXT_STYLE,
            md=6,
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody(
                    children=[
                        html.H5("Open Interest Relative Change"),
                        dbc.Row(
                            [
                                dbc.Col(html.P("Type")),
                                dbc.Col(html.P("Commercial")),
                                dbc.Col(html.P("Noncommercial")),
                                dbc.Col(html.P("Nonreportable")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(html.P("Current:")),
                                dbc.Col(html.P(id="Current Commercial")),
                                dbc.Col(html.P(id="Current Noncommercial")),
                                dbc.Col(html.P(id="Current Nonreportable")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(html.P("3 Month:")),
                                dbc.Col(html.P(id="3 Month Commercial")),
                                dbc.Col(html.P(id="3 Month Noncommercial")),
                                dbc.Col(html.P(id="3 Month Nonreportable")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(html.P("6 Month:")),
                                dbc.Col(html.P(id="6 Month Commercial")),
                                dbc.Col(html.P(id="6 Month Noncommercial")),
                                dbc.Col(html.P(id="6 Month Nonreportable")),
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(html.P("1 Year:")),
                                dbc.Col(html.P(id="1 Year Commercial")),
                                dbc.Col(html.P(id="1 Year Noncommercial")),
                                dbc.Col(html.P(id="1 Year Nonreportable")),
                            ]
                        ),
                    ]
                )
            ),
            style=TABLE_CARD_TEXT_STYLE,
            md=6,
            sm=12,
        ),
    ],
)

content_third_row = dbc.Row(
    [
        dbc.Col(
            children=[
                dcc.Graph(id="mainGraph"),
                html.P("Select data type:"),
                dcc.Dropdown(
                    options=columnOptions, value="OpenInterest", id="columnDropdown"
                ),
                html.P(""),
                html.P("Select asset:"),
                dcc.Dropdown(options=tableOptions, value="EUR", id="tableDropdown"),
            ],
            md=12,
        ),
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
        # content_first_row,
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
    Output(component_id="Current Commercial", component_property="children"),
    Output(component_id="Current Noncommercial", component_property="children"),
    Output(component_id="Current Nonreportable", component_property="children"),
    Output(component_id="3 Month Commercial", component_property="children"),
    Output(component_id="3 Month Noncommercial", component_property="children"),
    Output(component_id="3 Month Nonreportable", component_property="children"),
    Output(component_id="6 Month Commercial", component_property="children"),
    Output(component_id="6 Month Noncommercial", component_property="children"),
    Output(component_id="6 Month Nonreportable", component_property="children"),
    Output(component_id="1 Year Commercial", component_property="children"),
    Output(component_id="1 Year Noncommercial", component_property="children"),
    Output(component_id="1 Year Nonreportable", component_property="children"),
    Input("tables", "value"),
    Input("category", "value"),
)
def renderPieChart(tables, category):
    df = read_sql(tables, engine)
    current_commercial = functions.total_open_interest_commercial(df.iloc[0])
    current_noncommercial = functions.total_open_interest_noncommercial(df.iloc[0])
    current_nonreportable = functions.total_open_interest_nonreportable(df.iloc[0])
    cc_3month_change = int(
        functions.percentage_change(
            (functions.total_open_interest_commercial(df.iloc[0])),
            (functions.total_open_interest_commercial(df.iloc[11])),
        )
    )
    nc_3month_change = int(
        functions.percentage_change(
            functions.total_open_interest_noncommercial(df.iloc[0]),
            functions.total_open_interest_noncommercial(df.iloc[11]),
        )
    )
    nr_3month_change = int(
        functions.percentage_change(
            functions.total_open_interest_nonreportable(df.iloc[0]),
            functions.total_open_interest_nonreportable(df.iloc[11]),
        )
    )
    cc_6month_change = int(
        functions.percentage_change(
            (functions.total_open_interest_commercial(df.iloc[0])),
            (functions.total_open_interest_commercial(df.iloc[25])),
        )
    )
    nc_6month_change = int(
        functions.percentage_change(
            (functions.total_open_interest_noncommercial(df.iloc[0])),
            (functions.total_open_interest_noncommercial(df.iloc[25])),
        )
    )
    nr_6month_change = int(
        functions.percentage_change(
            (functions.total_open_interest_nonreportable(df.iloc[0])),
            (functions.total_open_interest_nonreportable(df.iloc[25])),
        )
    )
    cc_1year_change = int(
        functions.percentage_change(
            (functions.total_open_interest_commercial(df.iloc[0])),
            (functions.total_open_interest_commercial(df.iloc[51])),
        )
    )
    nc_1year_change = int(
        functions.percentage_change(
            (functions.total_open_interest_noncommercial(df.iloc[0])),
            (functions.total_open_interest_noncommercial(df.iloc[51])),
        )
    )
    nr_1year_change = int(
        functions.percentage_change(
            (functions.total_open_interest_nonreportable(df.iloc[0])),
            (functions.total_open_interest_nonreportable(df.iloc[51])),
        )
    )

    if category == "All":
        df = pd.DataFrame(
            [
                [
                    "Open Interest Commercial",
                    (functions.total_open_interest_commercial(df.iloc[0])),
                ],
                [
                    "Open Interest Noncommercial",
                    (functions.total_open_interest_noncommercial(df.iloc[0])),
                ],
                [
                    "Open Interest Nonreportable Positions",
                    (functions.total_open_interest_nonreportable(df.iloc[0])),
                ],
            ],
            columns=["type", "result"],
        )
        pieChart = px.pie(
            df,
            values="result",
            names="type",
            hole=0.6,
            color_discrete_sequence=[
                "#eff3ff",
                "#bdd7e7",
                "#6baed6",
                "#3182bd",
                "#08519c",
            ],
        )
    if category == "Commercial":

        df = pd.DataFrame(
            [
                [
                    "Short % Commercial",
                    (functions.commercial_short_percentage(df.iloc[0])),
                ],
                [
                    "Long % Commercial",
                    (functions.commercial_long_percentage(df.iloc[0])),
                ],
            ],
            columns=["type", "result"],
        )
        pieChart = px.pie(
            df,
            values="result",
            names="type",
            hole=0.6,
            color_discrete_sequence=[
                "#eff3ff",
                "#bdd7e7",
                "#6baed6",
                "#3182bd",
                "#08519c",
            ],
        )
    if category == "Noncommercial":

        df = pd.DataFrame(
            [
                [
                    "Short % Noncommercial",
                    (functions.non_commercial_short_percentage(df.iloc[0])),
                ],
                [
                    "Long % Noncommercial",
                    (functions.non_commercial_long_percentage(df.iloc[0])),
                ],
            ],
            columns=["type", "result"],
        )
        pieChart = px.pie(
            df,
            values="result",
            names="type",
            hole=0.6,
            color_discrete_sequence=[
                "#eff3ff",
                "#bdd7e7",
                "#6baed6",
                "#3182bd",
                "#08519c",
            ],
        )
    if category == "Nonreportable Positions":

        df = pd.DataFrame(
            [
                [
                    "Short % Nonreportable Positions",
                    (functions.nonreportable_short_percentage(df.iloc[0])),
                ],
                [
                    "Long % Nonreportable Positions",
                    (functions.nonreportable_long_percentage(df.iloc[0])),
                ],
            ],
            columns=["type", "result"],
        )
        pieChart = px.pie(
            df,
            values="result",
            names="type",
            hole=0.6,
            color_discrete_sequence=[
                "#eff3ff",
                "#bdd7e7",
                "#6baed6",
                "#3182bd",
                "#08519c",
            ],
        )
    pieChart.update_traces(rotation=20)
    pieChart.update(layout_showlegend=True)
    pieChart.update_layout(
        margin=dict(t=0, b=0, l=0, r=0),
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor="White",
        ),
    )
    return (
        pieChart,
        f"{current_commercial}",
        f"{current_noncommercial}",
        f"{current_nonreportable}",
        f"{cc_3month_change}%",
        f"{nc_3month_change}%",
        f"{nr_3month_change}%",
        f"{cc_6month_change}%",
        f"{nc_6month_change}%",
        f"{nr_6month_change}%",
        f"{cc_1year_change}%",
        f"{nc_1year_change}%",
        f"{nr_1year_change}%",
    )


@app.callback(
    Output(component_id="mainGraph", component_property="figure"),
    # Output(component_id="last", component_property="children"),
    # Output(component_id="average", component_property="children"),
    # Output(component_id="high", component_property="children"),
    # Output(component_id="low", component_property="children"),
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
        lineFig
        # int(df[selectedColumn].iloc[0]),
        # int(df[selectedColumn].mean()),
        # int(df[selectedColumn].max()),
        # int(df[selectedColumn].min()),
    )


if __name__ == "__main__":
    app.run_server(port="8085", debug=True)

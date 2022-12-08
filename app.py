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
                    html.Div("Contracts:"),
                    dcc.Dropdown(
                        id="tables",
                        options=tableOptions,
                        value="EUR",
                        clearable=False,
                    ),
                    html.Div("Categories:"),
                    dcc.Dropdown(
                        id="category",
                        options=pie_options,
                        value="Commercial",
                        clearable=False,
                    ),
                ]
            ),
            style=PIE_CARD_TEXT_STYLE,
        ),
        dbc.Col(
            children=[
                dbc.Card(
                    dbc.CardBody(
                        html.Div(
                            children=[
                                html.H5("Open Interest Relative Change"),
                                html.Table(
                                    children=[
                                        html.Tr(
                                            children=[
                                                html.Th(""),
                                                html.Th("Commercial"),
                                                html.Th("Noncommercial"),
                                                html.Th("Nonreportable"),
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td("Current:"),
                                                html.Td(
                                                    id="Current Relative Commercial"
                                                ),
                                                html.Td(
                                                    id="Current Relative Noncommercial"
                                                ),
                                                html.Td(
                                                    id="Current Relative Nonreportable"
                                                ),
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td("3 Month:"),
                                                html.Td(
                                                    id="3 Month Relative Commercial"
                                                ),
                                                html.Td(
                                                    id="3 Month Relative Noncommercial"
                                                ),
                                                html.Td(
                                                    id="3 Month Relative Nonreportable"
                                                ),
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td("6 Month:"),
                                                html.Td(
                                                    id="6 Month Relative Commercial"
                                                ),
                                                html.Td(
                                                    id="6 Month Relative Noncommercial"
                                                ),
                                                html.Td(
                                                    id="6 Month Relative Nonreportable"
                                                ),
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td("1 Year:"),
                                                html.Td(
                                                    id="1 Year Relative Commercial"
                                                ),
                                                html.Td(
                                                    id="1 Year Relative Noncommercial"
                                                ),
                                                html.Td(
                                                    id="1 Year Relative Nonreportable"
                                                ),
                                            ]
                                        ),
                                    ],
                                    style={
                                        "border-collapse": "collapse",
                                        "width": "100%",
                                    },
                                ),
                            ]
                        )
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        html.Div(
                            children=[
                                html.H5("Open Interest Absolute Change"),
                                html.Table(
                                    children=[
                                        html.Tr(
                                            children=[
                                                html.Th(""),
                                                html.Th("Commercial"),
                                                html.Th("Noncommercial"),
                                                html.Th("Nonreportable"),
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td("Current:"),
                                                html.Td(
                                                    id="Current Absolute Commercial"
                                                ),
                                                html.Td(
                                                    id="Current Absolute Noncommercial"
                                                ),
                                                html.Td(
                                                    id="Current Absolute Nonreportable"
                                                ),
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td("3 Month:"),
                                                html.Td(
                                                    id="3 Month Absolute Commercial"
                                                ),
                                                html.Td(
                                                    id="3 Month Absolute Noncommercial"
                                                ),
                                                html.Td(
                                                    id="3 Month Absolute Nonreportable"
                                                ),
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td("6 Month:"),
                                                html.Td(
                                                    id="6 Month Absolute Commercial"
                                                ),
                                                html.Td(
                                                    id="6 Month Absolute Noncommercial"
                                                ),
                                                html.Td(
                                                    id="6 Month Absolute Nonreportable"
                                                ),
                                            ]
                                        ),
                                        html.Tr(
                                            children=[
                                                html.Td("1 Year:"),
                                                html.Td(
                                                    id="1 Year Absolute Commercial"
                                                ),
                                                html.Td(
                                                    id="1 Year Absolute Noncommercial"
                                                ),
                                                html.Td(
                                                    id="1 Year Absolute Nonreportable"
                                                ),
                                            ]
                                        ),
                                    ],
                                    style={
                                        "border-collapse": "collapse",
                                        "width": "100%",
                                    },
                                ),
                            ]
                        )
                    )
                ),
            ],
        ),
    ],
)

content_third_row = dbc.Row(
    [
        dbc.Col(
            children=[
                dcc.Graph(id="mainGraph"),
                html.Div("Select category:"),
                dcc.Dropdown(
                    options=columnOptions, value="OpenInterest", id="columnDropdown"
                ),
                html.Br(),
                html.Div("Select contract:"),
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
        "/main.css",
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
    Output(component_id="Current Relative Commercial", component_property="children"),
    Output(
        component_id="Current Relative Noncommercial", component_property="children"
    ),
    Output(
        component_id="Current Relative Nonreportable", component_property="children"
    ),
    Output(component_id="3 Month Relative Commercial", component_property="children"),
    Output(
        component_id="3 Month Relative Noncommercial", component_property="children"
    ),
    Output(
        component_id="3 Month Relative Nonreportable", component_property="children"
    ),
    Output(component_id="6 Month Relative Commercial", component_property="children"),
    Output(
        component_id="6 Month Relative Noncommercial", component_property="children"
    ),
    Output(
        component_id="6 Month Relative Nonreportable", component_property="children"
    ),
    Output(component_id="1 Year Relative Commercial", component_property="children"),
    Output(component_id="1 Year Relative Noncommercial", component_property="children"),
    Output(component_id="1 Year Relative Nonreportable", component_property="children"),
    Output(component_id="Current Absolute Commercial", component_property="children"),
    Output(
        component_id="Current Absolute Noncommercial", component_property="children"
    ),
    Output(
        component_id="Current Absolute Nonreportable", component_property="children"
    ),
    Output(component_id="3 Month Absolute Commercial", component_property="children"),
    Output(
        component_id="3 Month Absolute Noncommercial", component_property="children"
    ),
    Output(
        component_id="3 Month Absolute Nonreportable", component_property="children"
    ),
    Output(component_id="6 Month Absolute Commercial", component_property="children"),
    Output(
        component_id="6 Month Absolute Noncommercial", component_property="children"
    ),
    Output(
        component_id="6 Month Absolute Nonreportable", component_property="children"
    ),
    Output(component_id="1 Year Absolute Commercial", component_property="children"),
    Output(component_id="1 Year Absolute Noncommercial", component_property="children"),
    Output(component_id="1 Year Absolute Nonreportable", component_property="children"),
    Input("tables", "value"),
    Input("category", "value"),
)
def renderPieChart(tables, category):
    df = read_sql(tables, engine)
    current_relative_commercial = functions.total_open_interest_commercial(df.iloc[0])
    current_relative_noncommercial = functions.total_open_interest_noncommercial(
        df.iloc[0]
    )
    current_relative_nonreportable = functions.total_open_interest_nonreportable(
        df.iloc[0]
    )
    current_absolute_commercial = current_relative_commercial
    current_absolute_noncommercial = current_relative_noncommercial
    current_absolute_nonreportable = current_relative_nonreportable

    cc_3month_relative_change = int(
        functions.percentage_change(
            (functions.total_open_interest_commercial(df.iloc[0])),
            (functions.total_open_interest_commercial(df.iloc[11])),
        )
    )
    nc_3month_relative_change = int(
        functions.percentage_change(
            functions.total_open_interest_noncommercial(df.iloc[0]),
            functions.total_open_interest_noncommercial(df.iloc[11]),
        )
    )
    nr_3month_relative_change = int(
        functions.percentage_change(
            functions.total_open_interest_nonreportable(df.iloc[0]),
            functions.total_open_interest_nonreportable(df.iloc[11]),
        )
    )
    cc_6month_relative_change = int(
        functions.percentage_change(
            (functions.total_open_interest_commercial(df.iloc[0])),
            (functions.total_open_interest_commercial(df.iloc[25])),
        )
    )
    nc_6month_relative_change = int(
        functions.percentage_change(
            (functions.total_open_interest_noncommercial(df.iloc[0])),
            (functions.total_open_interest_noncommercial(df.iloc[25])),
        )
    )
    nr_6month_relative_change = int(
        functions.percentage_change(
            (functions.total_open_interest_nonreportable(df.iloc[0])),
            (functions.total_open_interest_nonreportable(df.iloc[25])),
        )
    )
    cc_1year_relative_change = int(
        functions.percentage_change(
            (functions.total_open_interest_commercial(df.iloc[0])),
            (functions.total_open_interest_commercial(df.iloc[51])),
        )
    )
    nc_1year_relative_change = int(
        functions.percentage_change(
            (functions.total_open_interest_noncommercial(df.iloc[0])),
            (functions.total_open_interest_noncommercial(df.iloc[51])),
        )
    )
    nr_1year_relative_change = int(
        functions.percentage_change(
            (functions.total_open_interest_nonreportable(df.iloc[0])),
            (functions.total_open_interest_nonreportable(df.iloc[51])),
        )
    )
    cc_3month_absolute_change = int(
        functions.absolute_change(
            functions.total_open_interest_commercial(df.iloc[0]),
            functions.total_open_interest_commercial(df.iloc[11]),
        )
    )
    nc_3month_absolute_change = int(
        functions.absolute_change(
            functions.total_open_interest_noncommercial(df.iloc[0]),
            functions.total_open_interest_noncommercial(df.iloc[11]),
        )
    )
    nr_3month_absolute_change = int(
        functions.absolute_change(
            functions.total_open_interest_nonreportable(df.iloc[0]),
            functions.total_open_interest_nonreportable(df.iloc[11]),
        )
    )
    cc_6month_absolute_change = int(
        functions.absolute_change(
            (functions.total_open_interest_commercial(df.iloc[0])),
            (functions.total_open_interest_commercial(df.iloc[25])),
        )
    )
    nc_6month_absolute_change = int(
        functions.absolute_change(
            (functions.total_open_interest_noncommercial(df.iloc[0])),
            (functions.total_open_interest_noncommercial(df.iloc[25])),
        )
    )
    nr_6month_absolute_change = int(
        functions.absolute_change(
            (functions.total_open_interest_nonreportable(df.iloc[0])),
            (functions.total_open_interest_nonreportable(df.iloc[25])),
        )
    )
    cc_1year_absolute_change = int(
        functions.absolute_change(
            (functions.total_open_interest_commercial(df.iloc[0])),
            (functions.total_open_interest_commercial(df.iloc[51])),
        )
    )
    nc_1year_absolute_change = int(
        functions.absolute_change(
            (functions.total_open_interest_noncommercial(df.iloc[0])),
            (functions.total_open_interest_noncommercial(df.iloc[51])),
        )
    )
    nr_1year_absolute_change = int(
        functions.absolute_change(
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
        f"{current_relative_commercial}",
        f"{current_relative_noncommercial}",
        f"{current_relative_nonreportable}",
        f"{cc_3month_relative_change}%",
        f"{nc_3month_relative_change}%",
        f"{nr_3month_relative_change}%",
        f"{cc_6month_relative_change}%",
        f"{nc_6month_relative_change}%",
        f"{nr_6month_relative_change}%",
        f"{cc_1year_relative_change}%",
        f"{nc_1year_relative_change}%",
        f"{nr_1year_relative_change}%",
        f"{current_absolute_commercial}",
        f"{current_absolute_noncommercial}",
        f"{current_absolute_nonreportable}",
        f"{cc_3month_absolute_change}",
        f"{nc_3month_absolute_change}",
        f"{nr_3month_absolute_change}",
        f"{cc_6month_absolute_change}",
        f"{nc_6month_absolute_change}",
        f"{nr_6month_absolute_change}",
        f"{cc_1year_absolute_change}",
        f"{nc_1year_absolute_change}",
        f"{nr_1year_absolute_change}",
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

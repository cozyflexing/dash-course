from turtle import position
import pandas as pd

extracted_data = pd.read_csv(f"data/CFTC_USD.csv", nrows=1)

noncommercial_percentage_of_total_oi = (
    extracted_data["Noncommercial Net Position"] / extracted_data["Open Interest"]
) * 100

commercial_percentage_of_total_oi = (
    extracted_data["Commercial Net Position"] / extracted_data["Open Interest"]
) * 100

short_percentage_of_noncommercial_oi = (
    extracted_data["Noncommercial Short"]
    / (extracted_data["Noncommercial Long"] + extracted_data["Noncommercial Short"])
) * 100

short_percentage_of_commercial_oi = (
    extracted_data["Commercial Short"]
    / (extracted_data["Commercial Long"] + extracted_data["Commercial Short"])
) * 100

long_percentage_of_commercial_oi = (
    extracted_data["Commercial Long"]
    / (extracted_data["Commercial Long"] + extracted_data["Commercial Short"])
) * 100

long_percentage_of_noncommercial_oi = (
    extracted_data["Noncommercial Long"]
    / (extracted_data["Noncommercial Long"] + extracted_data["Noncommercial Short"])
) * 100

short_percentage_of_total_oi = (
    extracted_data["Total Short"] / extracted_data["Open Interest"] * 100
)

long_percentage_of_total_oi = (
    extracted_data["Total Long"] / extracted_data["Open Interest"] * 100
)

########
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dcc, dash, html
import plotly.express as px
import pandas as pd
import data_calculations as dcalc
import pathlib

app = dash.Dash(
    __name__,
    title="sixteenanalytics",
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
    ],
)


def get_pandas_data(csv_filename: str) -> pd.DataFrame:
    """
    Load data from /data directory as a pandas DataFrame
    using relative paths. Relative paths are necessary for
    data loading to work in Heroku.
    """
    PATH = pathlib.Path(__file__).parent
    DATA_PATH = PATH.joinpath("data").resolve()
    return pd.read_csv(DATA_PATH.joinpath(csv_filename))


data_options = [
    "Open Interest",
    "Noncommercial Long",
    "Noncommercial Short",
    "Noncommercial Spreads",
    "Commercial Long",
    "Commercial Short",
    "Total Long",
    "Total Short",
    "Nonreportable Positions Long",
    "Nonreportable Positions Short",
    "Commercial Net Position",
    "Noncommercial Net Position",
]

asset_options = [
    "EURO",
    "USD",
    "GBP",
    "CAD",
    "JPY",
    "AUD",
    "NZD",
    "CHF",
    "SILVER",
    "GOLD",
    "WTI",
    "NASDAQ",
    "SP500",
    "DJIA",
]

look_back_options = [
    "6 months",
    "1 year",
    "3 years",
    "5 years",
    "Max",
]

calc_options = [
    "Commercial COT Index",
    "Noncommercial COT Index",
    "Commercial COT Movement Index",
    "Noncommercial COT Movement Index",
]

ratio_options = [
    "Commercial percentage of total open interest",
    "Noncommercial percentage of total open interest",
    "Short percentage of commercial open interest",
    "Short percentage of noncommercial open interest",
    "Long percentage of commercial open interest",
    "Long percentage of noncommercial open interest",
]


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

content = html.Div(
    id="page-content",
    children=[],
    style=CONTENT_STYLE,
)

sidebar = html.Div(
    [
        html.H2(
            "Sixteenanalytics", style={"textAlign": "center", "font-size": "1.75rem"}
        ),
        html.Hr(),
        html.P(
            "Graph options",
            style={"textAlign": "center", "font-size": "1.25rem"},
        ),
        dbc.Nav(
            [
                dbc.NavLink("CFTC", href="/", active="exact"),
                dbc.NavLink("COT", href="/COT-CALCULATIONS", active="exact"),
                dbc.NavLink("RATIOS", href="/RATIOS", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


app.layout = html.Div(
    children=[
        dcc.Location(id="url"),
        html.Div(children=sidebar, className="testgriditem"),
        html.Div(children=content, className="testgriditem"),
    ],
    className="testgrid",
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [
            html.H1("CFTC Data", style={"textAlign": "center"}),
            html.Div(
                className="chartgrid",
                children=[
                    html.Div(className="griditem", id="avergae_cftc"),
                    html.Div(className="griditem", id="previous_cftc"),
                    html.Div(className="griditem", id="current_cftc"),
                    html.Div(className="griditem", id="change_cftc"),
                    html.Div(
                        className="griditem grid-col-span-4",
                        children=[
                            dcc.Graph(id="cftc_graph"),
                            dcc.Dropdown(
                                id="asset_options",
                                options=asset_options,
                                value="NASDAQ",
                                className="m-1",
                            ),
                            dcc.Dropdown(
                                id="data_options",
                                options=data_options,
                                value="Open Interest",
                                className="m-1",
                            ),
                            dcc.Dropdown(
                                id="lookback",
                                options=look_back_options,
                                value="1 year",
                                className="m-1",
                            ),
                        ],
                    ),
                ],
            ),
        ]
    elif pathname == "/COT-CALCULATIONS":
        return [
            html.H1("COT Calculations", style={"textAlign": "center"}),
            html.Div(
                className="chartgrid",
                children=[
                    html.Div(className="griditem", id="avergae_cot"),
                    html.Div(className="griditem", id="previous_cot"),
                    html.Div(className="griditem", id="current_cot"),
                    html.Div(className="griditem", id="change_cot"),
                    html.Div(
                        className="griditem grid-col-span-4",
                        children=[
                            dcc.Graph(id="cot_graph"),
                            dcc.Dropdown(
                                id="asset_options_cot",
                                options=asset_options,
                                value="NASDAQ",
                                className="m-1",
                            ),
                            dcc.Dropdown(
                                id="cot_options",
                                options=calc_options,
                                value="Commercial COT Index",
                                className="m-1",
                            ),
                            dcc.Dropdown(
                                id="lookback_cot",
                                options=look_back_options,
                                value="1 year",
                                className="m-1",
                            ),
                        ],
                    ),
                ],
            ),
        ]
    elif pathname == "/RATIOS":
        return [
            html.H1("RATIOS", style={"textAlign": "center"}),
            html.Div(
                className="chartgrid",
                children=[
                    html.Div(className="griditem", id="avergae_ratio"),
                    html.Div(className="griditem", id="previous_ratio"),
                    html.Div(className="griditem", id="current_ratio"),
                    html.Div(className="griditem", id="change_ratio"),
                    html.Div(
                        className="griditem grid-col-span-4",
                        children=[
                            dcc.Graph(id="ratio_garph"),
                            dcc.Dropdown(
                                id="asset_options_ratio",
                                options=asset_options,
                                value="NASDAQ",
                                className="m-1",
                            ),
                            dcc.Dropdown(
                                id="ratio_options",
                                options=ratio_options,
                                value="Commercial percentage of total open interest",
                                className="m-1",
                            ),
                            dcc.Dropdown(
                                id="lookback_ratio",
                                options=look_back_options,
                                value="1 year",
                                className="m-1",
                            ),
                        ],
                    ),
                ],
            ),
        ]

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


@app.callback(
    Output(component_id="cftc_graph", component_property="figure"),
    Output(component_id="avergae_cftc", component_property="children"),
    Output(component_id="previous_cftc", component_property="children"),
    Output(component_id="current_cftc", component_property="children"),
    Output(component_id="change_cftc", component_property="children"),
    Input(component_id="asset_options", component_property="value"),
    Input(component_id="data_options", component_property="value"),
    Input(component_id="lookback", component_property="value"),
)
def cftc_graph(selected_asset, selected_data, selected_lookback):
    if selected_lookback == "6 months":
        extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
        extracted_data = extracted_data.head(26)
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
    elif selected_lookback == "1 year":
        extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
        extracted_data = extracted_data.head(52)
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
    elif selected_lookback == "3 years":
        extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
        extracted_data = extracted_data.head(156)
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
    elif selected_lookback == "5 years":
        extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
        extracted_data = extracted_data.head(260)
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
    elif selected_lookback == "Max":
        extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
    avergae_cftc = f"The average {selected_data.lower()}: {int(extracted_data[f'{selected_data}'].mean())}"
    previous_cftc = f"The previous {selected_data.lower()}: {int(extracted_data[f'{selected_data}'][1])}"
    current_cftc = f"The current {selected_data.lower()}: {int(extracted_data[f'{selected_data}'][0])}"
    change_cftc = f"The change in {selected_data.lower()}: {int(extracted_data[f'{selected_data}'][0]-extracted_data[f'{selected_data}'][1])}"
    return line_fig, avergae_cftc, previous_cftc, current_cftc, change_cftc


@app.callback(
    Output(component_id="cot_graph", component_property="figure"),
    Output(component_id="avergae_cot", component_property="children"),
    Output(component_id="previous_cot", component_property="children"),
    Output(component_id="current_cot", component_property="children"),
    Output(component_id="change_cot", component_property="children"),
    Input(component_id="asset_options_cot", component_property="value"),
    Input(component_id="cot_options", component_property="value"),
    Input(component_id="lookback_cot", component_property="value"),
)
def cot_graph(selected_asset, selected_calculation, selected_lookback):
    cot_index, copy_of_cot_index, cot_movement_index = [], [], []
    if selected_calculation == "Commercial COT Index":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
        elif selected_lookback == "1 year":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(52)
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
        elif selected_lookback == "3 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(156)
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
        elif selected_lookback == "5 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(260)
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
        else:
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
        avergae_cot = f"The average {selected_calculation.lower()}: {round(sum(cot_index) / len(cot_index))}"
        previous_cot = (
            f"The previous {selected_calculation.lower()}: {round(cot_index[1])}"
        )
        current_cot = (
            f"The current {selected_calculation.lower()}: {round(cot_index[0])}"
        )
        change_cot = f"The change in {selected_calculation.lower()}: {round(cot_index[0] - cot_index[1])}"
        if selected_lookback == "1 year":
            title = (
                f"The {selected_calculation} for {selected_asset} over the past year"
            )
        else:
            title = f"The {selected_calculation} for {selected_asset} over the past {selected_lookback}"
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=cot_index,
            title=title,
            labels={
                "y": "Index",
                "x": "Dates",
            },
        )
        line_fig.add_hrect(
            y0=5, y1=-1, line_width=0, fillcolor="red", opacity=0.2
        ).add_hrect(y0=90, y1=101, line_width=0, fillcolor="green", opacity=0.2)
    if selected_calculation == "Noncommercial COT Index":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
        elif selected_lookback == "1 year":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(52)
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
        elif selected_lookback == "3 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(156)
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
        elif selected_lookback == "5 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(260)
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
        else:
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
        avergae_cot = f"The average {selected_calculation.lower()}: {round(sum(cot_index) / len(cot_index))}"
        previous_cot = (
            f"The previous {selected_calculation.lower()}: {round(cot_index[1])}"
        )
        current_cot = (
            f"The current {selected_calculation.lower()}: {round(cot_index[0])}"
        )
        change_cot = f"The change in {selected_calculation.lower()}: {round(cot_index[0] - cot_index[1])}"
        if selected_lookback == "1 year":
            title = (
                f"The {selected_calculation} for {selected_asset} over the past year"
            )
        else:
            title = f"The {selected_calculation} for {selected_asset} over the past {selected_lookback}"
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=cot_index,
            title=title,
            labels={
                "y": "Index",
                "x": "Dates",
            },
        )
        line_fig.add_hrect(
            y0=5, y1=-1, line_width=0, fillcolor="red", opacity=0.2
        ).add_hrect(y0=90, y1=101, line_width=0, fillcolor="green", opacity=0.2)
    if selected_calculation == "Commercial COT Movement Index":
        line_fig = px.line(
            template="plotly_white",
        )
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
            for x in cot_index:
                copy_of_cot_index.append(x)
                if len(copy_of_cot_index) >= 7:
                    difference = copy_of_cot_index[-7] - copy_of_cot_index[-1]
                    cot_movement_index.append(difference)
        elif selected_lookback == "1 year":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(52)
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
            for x in cot_index:
                copy_of_cot_index.append(x)
                if len(copy_of_cot_index) >= 7:
                    difference = copy_of_cot_index[-7] - copy_of_cot_index[-1]
                    cot_movement_index.append(difference)
        elif selected_lookback == "3 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(156)
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
            for x in cot_index:
                copy_of_cot_index.append(x)
                if len(copy_of_cot_index) >= 7:
                    difference = copy_of_cot_index[-7] - copy_of_cot_index[-1]
                    cot_movement_index.append(difference)
        elif selected_lookback == "5 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(260)
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
            for x in cot_index:
                copy_of_cot_index.append(x)
                if len(copy_of_cot_index) >= 7:
                    difference = copy_of_cot_index[-7] - copy_of_cot_index[-1]
                    cot_movement_index.append(difference)
        else:
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
            for x in cot_index:
                copy_of_cot_index.append(x)
                if len(copy_of_cot_index) >= 7:
                    difference = copy_of_cot_index[-7] - copy_of_cot_index[-1]
                    cot_movement_index.append(difference)
        avergae_cot = f"The average {selected_calculation.lower()}: {round(sum(cot_movement_index) / len(cot_movement_index))}"
        previous_cot = f"The previous {selected_calculation.lower()}: {round(cot_movement_index[1])}"
        current_cot = f"The current {selected_calculation.lower()}: {round(cot_movement_index[0])}"
        change_cot = f"The change in {selected_calculation.lower()}: {round(cot_movement_index[0] - cot_movement_index[1])}"
        if selected_lookback == "1 year":
            title = (
                f"The {selected_calculation} for {selected_asset} over the past year"
            )
        else:
            title = f"The {selected_calculation} for {selected_asset} over the past {selected_lookback}"
        line_fig = px.bar(
            x=extracted_data["Date"][6:],
            y=cot_movement_index,
            template="plotly_white",
            title=title,
            labels={
                "y": "Index",
                "x": "Dates",
            },
        )
    if selected_calculation == "Noncommercial COT Movement Index":
        line_fig = px.line(
            template="plotly_white",
        )
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
            for x in cot_index:
                copy_of_cot_index.append(x)
                if len(copy_of_cot_index) >= 7:
                    difference = copy_of_cot_index[-7] - copy_of_cot_index[-1]
                    cot_movement_index.append(difference)
        elif selected_lookback == "1 year":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(52)
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
            for x in cot_index:
                copy_of_cot_index.append(x)
                if len(copy_of_cot_index) >= 7:
                    difference = copy_of_cot_index[-7] - copy_of_cot_index[-1]
                    cot_movement_index.append(difference)
        elif selected_lookback == "3 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(156)
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
            for x in cot_index:
                copy_of_cot_index.append(x)
                if len(copy_of_cot_index) >= 7:
                    difference = copy_of_cot_index[-7] - copy_of_cot_index[-1]
                    cot_movement_index.append(difference)
        elif selected_lookback == "5 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(260)
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
            for x in cot_index:
                copy_of_cot_index.append(x)
                if len(copy_of_cot_index) >= 7:
                    difference = copy_of_cot_index[-7] - copy_of_cot_index[-1]
                    cot_movement_index.append(difference)
        else:
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
            for x in cot_index:
                copy_of_cot_index.append(x)
                if len(copy_of_cot_index) >= 7:
                    difference = copy_of_cot_index[-7] - copy_of_cot_index[-1]
                    cot_movement_index.append(difference)
        avergae_cot = f"The average {selected_calculation.lower()}: {round(sum(cot_movement_index) / len(cot_movement_index))}"
        previous_cot = f"The previous {selected_calculation.lower()}: {round(cot_movement_index[1])}"
        current_cot = f"The current {selected_calculation.lower()}: {round(cot_movement_index[0])}"
        change_cot = f"The change in {selected_calculation.lower()}: {round(cot_movement_index[0] - cot_movement_index[1])}"
        if selected_lookback == "1 year":
            title = (
                f"The {selected_calculation} for {selected_asset} over the past year"
            )
        else:
            title = f"The {selected_calculation} for {selected_asset} over the past {selected_lookback}"
        line_fig = px.bar(
            x=extracted_data["Date"][6:],
            y=cot_movement_index,
            template="plotly_white",
            title=title,
            labels={
                "y": "Index",
                "x": "Dates",
            },
        )
    return line_fig, avergae_cot, previous_cot, current_cot, change_cot


@app.callback(
    Output(component_id="ratio_garph", component_property="figure"),
    Output(component_id="avergae_ratio", component_property="children"),
    Output(component_id="previous_ratio", component_property="children"),
    Output(component_id="current_ratio", component_property="children"),
    Output(component_id="change_ratio", component_property="children"),
    Input(component_id="asset_options_ratio", component_property="value"),
    Input(component_id="ratio_options", component_property="value"),
    Input(component_id="lookback_ratio", component_property="value"),
)
def ratio_graph(selected_asset, selected_ratio, selected_lookback):
    if selected_ratio == "Commercial percentage of total open interest":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    extracted_data["Commercial Net Position"]
                    / extracted_data["Open Interest"]
                )
                * 100,
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "1 year":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(52)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past year.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    extracted_data["Commercial Net Position"]
                    / extracted_data["Open Interest"]
                )
                * 100,
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "3 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(156)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    extracted_data["Commercial Net Position"]
                    / extracted_data["Open Interest"]
                )
                * 100,
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "5 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(260)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    extracted_data["Commercial Net Position"]
                    / extracted_data["Open Interest"]
                )
                * 100,
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "Max":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    extracted_data["Commercial Net Position"]
                    / extracted_data["Open Interest"]
                )
                * 100,
                labels={"y": "Percentage", "x": "Dates"},
            )

        needed_data = (
            extracted_data["Commercial Net Position"] / extracted_data["Open Interest"]
        ) * 100
        avergae_ratio = (
            f"The average {selected_ratio.lower()}: {round(needed_data.mean(),2)}"
        )
        previous_ratio = (
            f"The previous {selected_ratio.lower()}: {round(needed_data[1],2)}"
        )
        current_ratio = (
            f"The current {selected_ratio.lower()}: {round(needed_data[0],2)}"
        )
        change_ratio = f"The change in {selected_ratio.lower()}: {round(needed_data[0] - needed_data[1],2)}"
    if selected_ratio == "Noncommercial percentage of total open interest":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    extracted_data["Noncommercial Net Position"]
                    / extracted_data["Open Interest"]
                )
                * 100,
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "1 year":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(52)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past year.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    extracted_data["Noncommercial Net Position"]
                    / extracted_data["Open Interest"]
                )
                * 100,
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "3 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(156)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    extracted_data["Noncommercial Net Position"]
                    / extracted_data["Open Interest"]
                )
                * 100,
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "5 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(260)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    extracted_data["Noncommercial Net Position"]
                    / extracted_data["Open Interest"]
                )
                * 100,
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "Max":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    extracted_data["Noncommercial Net Position"]
                    / extracted_data["Open Interest"]
                )
                * 100,
                labels={"y": "Percentage", "x": "Dates"},
            )
        needed_data = (
            extracted_data["Noncommercial Net Position"]
            / extracted_data["Open Interest"]
        ) * 100
        avergae_ratio = (
            f"The average {selected_ratio.lower()}: {round(needed_data.mean(),2)}"
        )
        previous_ratio = (
            f"The previous {selected_ratio.lower()}: {round(needed_data[1],2)}"
        )
        current_ratio = (
            f"The current {selected_ratio.lower()}: {round(needed_data[0],2)}"
        )
        change_ratio = f"The change in {selected_ratio.lower()}: {round(needed_data[0] - needed_data[1],2)}"
    if selected_ratio == "Short percentage of commercial open interest":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Commercial Short"]
                        / (
                            extracted_data["Commercial Long"]
                            + extracted_data["Commercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "1 year":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(52)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past year.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Commercial Short"]
                        / (
                            extracted_data["Commercial Long"]
                            + extracted_data["Commercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "3 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(156)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Commercial Short"]
                        / (
                            extracted_data["Commercial Long"]
                            + extracted_data["Commercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "5 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(260)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Commercial Short"]
                        / (
                            extracted_data["Commercial Long"]
                            + extracted_data["Commercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "Max":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Commercial Short"]
                        / (
                            extracted_data["Commercial Long"]
                            + extracted_data["Commercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        needed_data = (
            extracted_data["Commercial Short"]
            / (extracted_data["Commercial Long"] + extracted_data["Commercial Short"])
        ) * 100
        avergae_ratio = (
            f"The average {selected_ratio.lower()}: {round(needed_data.mean(),2)}"
        )
        previous_ratio = (
            f"The previous {selected_ratio.lower()}: {round(needed_data[1],2)}"
        )
        current_ratio = (
            f"The current {selected_ratio.lower()}: {round(needed_data[0],2)}"
        )
        change_ratio = f"The change in {selected_ratio.lower()}: {round(needed_data[0] - needed_data[1],2)}"
    if selected_ratio == "Short percentage of noncommercial open interest":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Noncommercial Short"]
                        / (
                            extracted_data["Noncommercial Long"]
                            + extracted_data["Noncommercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "1 year":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(52)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past year.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Noncommercial Short"]
                        / (
                            extracted_data["Noncommercial Long"]
                            + extracted_data["Noncommercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "3 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(156)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Noncommercial Short"]
                        / (
                            extracted_data["Noncommercial Long"]
                            + extracted_data["Noncommercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "5 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(260)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Noncommercial Short"]
                        / (
                            extracted_data["Noncommercial Long"]
                            + extracted_data["Noncommercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "Max":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Noncommercial Short"]
                        / (
                            extracted_data["Noncommercial Long"]
                            + extracted_data["Noncommercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        needed_data = (
            extracted_data["Noncommercial Short"]
            / (
                extracted_data["Noncommercial Long"]
                + extracted_data["Noncommercial Short"]
            )
        ) * 100
        avergae_ratio = (
            f"The average {selected_ratio.lower()}: {round(needed_data.mean(),2)}"
        )
        previous_ratio = (
            f"The previous {selected_ratio.lower()}: {round(needed_data[1],2)}"
        )
        current_ratio = (
            f"The current {selected_ratio.lower()}: {round(needed_data[0],2)}"
        )
        change_ratio = f"The change in {selected_ratio.lower()}: {round(needed_data[0] - needed_data[1],2)}"
    if selected_ratio == "Long percentage of commercial open interest":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Commercial Long"]
                        / (
                            extracted_data["Commercial Long"]
                            + extracted_data["Commercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "1 year":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(52)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past year.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Commercial Long"]
                        / (
                            extracted_data["Commercial Long"]
                            + extracted_data["Commercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "3 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(156)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Commercial Long"]
                        / (
                            extracted_data["Commercial Long"]
                            + extracted_data["Commercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "5 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(260)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Commercial Long"]
                        / (
                            extracted_data["Commercial Long"]
                            + extracted_data["Commercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "Max":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Commercial Long"]
                        / (
                            extracted_data["Commercial Long"]
                            + extracted_data["Commercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        needed_data = (
            extracted_data["Commercial Long"]
            / (extracted_data["Commercial Long"] + extracted_data["Commercial Short"])
        ) * 100
        avergae_ratio = (
            f"The average {selected_ratio.lower()}: {round(needed_data.mean(),2)}"
        )
        previous_ratio = (
            f"The previous {selected_ratio.lower()}: {round(needed_data[1],2)}"
        )
        current_ratio = (
            f"The current {selected_ratio.lower()}: {round(needed_data[0],2)}"
        )
        change_ratio = f"The change in {selected_ratio.lower()}: {round(needed_data[0] - needed_data[1],2)}"
    if selected_ratio == "Long percentage of noncommercial open interest":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Noncommercial Long"]
                        / (
                            extracted_data["Noncommercial Long"]
                            + extracted_data["Noncommercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "1 year":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(52)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past year.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Noncommercial Long"]
                        / (
                            extracted_data["Noncommercial Long"]
                            + extracted_data["Noncommercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "3 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(156)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Noncommercial Long"]
                        / (
                            extracted_data["Noncommercial Long"]
                            + extracted_data["Noncommercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "5 years":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(260)
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Noncommercial Long"]
                        / (
                            extracted_data["Noncommercial Long"]
                            + extracted_data["Noncommercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        elif selected_lookback == "Max":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            line_fig = px.line(
                title=f"The {selected_ratio} for {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    (
                        extracted_data["Noncommercial Long"]
                        / (
                            extracted_data["Noncommercial Long"]
                            + extracted_data["Noncommercial Short"]
                        )
                    )
                    * 100
                ),
                labels={"y": "Percentage", "x": "Dates"},
            )
        needed_data = (
            extracted_data["Noncommercial Long"]
            / (
                extracted_data["Noncommercial Long"]
                + extracted_data["Noncommercial Short"]
            )
        ) * 100
        avergae_ratio = (
            f"The average {selected_ratio.lower()}: {round(needed_data.mean(),2)}"
        )
        previous_ratio = (
            f"The previous {selected_ratio.lower()}: {round(needed_data[1],2)}"
        )
        current_ratio = (
            f"The current {selected_ratio.lower()}: {round(needed_data[0],2)}"
        )
        change_ratio = f"The change in {selected_ratio.lower()}: {round(needed_data[0] - needed_data[1],2)}"

    return line_fig, avergae_ratio, previous_ratio, current_ratio, change_ratio


if __name__ == "__main__":
    app.run_server(debug=True)

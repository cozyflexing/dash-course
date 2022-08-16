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
]

look_back_options = [
    "6 months",
    "1 year",
    "3 years",
    "5 years",
    "Max",
]

calc_options = [
    "COT Index Commercial",
    "COT Index Noncommercial",
    "COT Movement Index Commercial",
    "COT Movement Index Noncommercial",
]

ratio_options = [
    "Commercial percentage of total open interest",
    "Noncommercial percentage of total open interest",
    "Short percentage of commercial open interest",
    "Short percentage of noncommercial open interest",
    "Long percentage of commercial open interest",
    "Long percentage of noncommercial open interest",
]


# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

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

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return [
            html.H1("CFTC Data", style={"textAlign": "center"}),
            dcc.Graph(id="regular_data_graph"),
            dcc.Dropdown(
                id="asset_options",
                options=asset_options,
                value="USD",
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
        ]
    elif pathname == "/COT-CALCULATIONS":
        return [
            html.H1("COT Calculations", style={"textAlign": "center"}),
            dcc.Graph(id="calculated_data_garph"),
            dcc.Dropdown(
                id="asset_options_calc",
                options=asset_options,
                value="NASDAQ",
                className="m-1",
            ),
            dcc.Dropdown(
                id="calc_options",
                options=calc_options,
                value="COT Index Commercial",
                className="m-1",
            ),
            dcc.Dropdown(
                id="lookback_calc",
                options=look_back_options,
                value="1 year",
                className="m-1",
            ),
        ]
    elif pathname == "/RATIOS":
        return [
            html.H1("RATIOS", style={"textAlign": "center"}),
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
    Output(component_id="regular_data_graph", component_property="figure"),
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
    return line_fig


@app.callback(
    Output(component_id="calculated_data_garph", component_property="figure"),
    Input(component_id="asset_options_calc", component_property="value"),
    Input(component_id="calc_options", component_property="value"),
    Input(component_id="lookback_calc", component_property="value"),
)
def cot_graph(selected_asset, selected_calculation, selected_lookback):
    cot_index, copy_of_cot_index, cot_movement_index = [], [], []
    if selected_calculation == "COT Index Commercial":
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
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=cot_index,
            labels={
                "y": f"{selected_calculation} {selected_asset}",
                "x": "Dates",
            },
        )
        line_fig.add_hrect(
            y0=5, y1=-1, line_width=0, fillcolor="red", opacity=0.2
        ).add_hrect(y0=90, y1=101, line_width=0, fillcolor="green", opacity=0.2)
    if selected_calculation == "COT Index Noncommercial":
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
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=cot_index,
            labels={
                "y": f"{selected_calculation} {selected_asset}",
                "x": "Dates",
            },
        )
        line_fig.add_hrect(
            y0=5, y1=-1, line_width=0, fillcolor="red", opacity=0.2
        ).add_hrect(y0=90, y1=101, line_width=0, fillcolor="green", opacity=0.2)
    if selected_calculation == "COT Movement Index Commercial":
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
        line_fig = px.bar(
            x=extracted_data["Date"][6:],
            y=cot_movement_index,
            template="plotly_white",
            labels={
                "y": f"{selected_calculation} {selected_asset}",
                "x": "Dates",
            },
        )
    if selected_calculation == "COT Movement Index Noncommercial":
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
        line_fig = px.bar(
            x=extracted_data["Date"][6:],
            y=cot_movement_index,
            template="plotly_white",
            labels={
                "y": f"{selected_calculation} {selected_asset}",
                "x": "Dates",
            },
        )
    return line_fig


@app.callback(
    Output(component_id="ratio_garph", component_property="figure"),
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    extracted_data["Commercial Net Position"]
                    / extracted_data["Open Interest"]
                )
                * 100,
                labels={"y": "Percentage", "x": "Dates"},
            )
    if selected_ratio == "Noncommercial percentage of total open interest":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            line_fig = px.line(
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
                template="plotly_white",
                x=extracted_data["Date"],
                y=(
                    extracted_data["Noncommercial Net Position"]
                    / extracted_data["Open Interest"]
                )
                * 100,
                labels={"y": "Percentage", "x": "Dates"},
            )
    if selected_ratio == "Short percentage of commercial open interest":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            line_fig = px.line(
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
    if selected_ratio == "Short percentage of noncommercial open interest":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            line_fig = px.line(
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
    if selected_ratio == "Long percentage of commercial open interest":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            line_fig = px.line(
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
    if selected_ratio == "Long percentage of noncommercial open interest":
        if selected_lookback == "6 months":
            extracted_data = get_pandas_data(f"CFTC_{selected_asset}.csv")
            extracted_data = extracted_data.head(26)
            line_fig = px.line(
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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
                title=f"The {selected_ratio} for the {selected_asset} over the past {selected_lookback}.",
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

    return line_fig


if __name__ == "__main__":
    app.run_server(debug=True)

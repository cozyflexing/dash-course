import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash import dcc, dash, html
import plotly.express as px
import pandas as pd
import data_calculations as dcalc

app = dash.Dash(
    __name__,
    title="sixteenanalytics",
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
    ],
)


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
    "6 Months",
    "1 Year",
    "3 Years",
    "5 Years",
    "Max",
]

calc_options = [
    "COT Index Commercial",
    "COT Index Noncommercial",
    "COT Movement Index Commercial",
    "COT Movement Index Noncommercial",
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
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
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
                value="1 Year",
                className="m-1",
            ),
            dcc.Graph(id="regular_data_graph"),
        ]
    elif pathname == "/COT-CALCULATIONS":
        return [
            html.H1("COT Calculations", style={"textAlign": "center"}),
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
                value="1 Year",
                className="m-1",
            ),
            dcc.Graph(id="calculated_data_garph"),
        ]
    elif pathname == "/page-2":
        return [
            html.H1("High School in Iran", style={"textAlign": "center"}),
            dcc.Graph(id="linegraph", figure=px.line(df, x="Date", y="Open Interest")),
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
def standard_graph_update(selected_asset, selected_data, selected_lookback):
    if selected_lookback == "6 Months":
        extracted_data = pd.read_csv(f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=26)
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
    elif selected_lookback == "1 Year":
        extracted_data = pd.read_csv(f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=52)
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
    elif selected_lookback == "3 Years":
        extracted_data = pd.read_csv(f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=156)
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
    elif selected_lookback == "5 Years":
        extracted_data = pd.read_csv(f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=260)
        line_fig = px.line(
            template="plotly_white",
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
    elif selected_lookback == "Max":
        extracted_data = pd.read_csv(f"CSV_FILES/CFTC_{selected_asset}.csv")
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
def calculated_grap_update(selected_asset, selected_calculation, selected_lookback):
    cot_index, copy_of_cot_index, cot_movement_index = [], [], []
    if selected_calculation == "COT Index Commercial":
        if selected_lookback == "6 Months":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=26
            )
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
        elif selected_lookback == "1 Year":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=52
            )
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
        elif selected_lookback == "3 Year":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=156
            )
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
        elif selected_lookback == "5 Year":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=260
            )
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
        else:
            extracted_data = pd.read_csv(f"CSV_FILES/CFTC_{selected_asset}.csv")
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
            y0=5, y1=-1, line_width=0, fillcolor="red", opacity=0.5
        ).add_hrect(y0=90, y1=101, line_width=0, fillcolor="green", opacity=0.5)
    if selected_calculation == "COT Index Noncommercial":
        if selected_lookback == "6 Months":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=26
            )
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
        elif selected_lookback == "1 Year":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=52
            )
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
        elif selected_lookback == "3 Year":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=156
            )
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
        elif selected_lookback == "5 Year":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=260
            )
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
        else:
            extracted_data = pd.read_csv(f"CSV_FILES/CFTC_{selected_asset}.csv")
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
            y0=5, y1=-1, line_width=0, fillcolor="red", opacity=0.5
        ).add_hrect(y0=90, y1=101, line_width=0, fillcolor="green", opacity=0.5)
    if selected_calculation == "COT Movement Index Commercial":
        line_fig = px.line(
            template="plotly_white",
        )
        if selected_lookback == "6 Months":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=26
            )
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
        elif selected_lookback == "1 Year":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=52
            )
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
        elif selected_lookback == "3 Years":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=156
            )
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
        elif selected_lookback == "5 Years":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=260
            )
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
            extracted_data = pd.read_csv(f"CSV_FILES/CFTC_{selected_asset}.csv")
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
        if selected_lookback == "6 Months":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=26
            )
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
        elif selected_lookback == "1 Year":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=52
            )
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
        elif selected_lookback == "3 Years":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=156
            )
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
        elif selected_lookback == "5 Years":
            extracted_data = pd.read_csv(
                f"CSV_FILES/CFTC_{selected_asset}.csv", nrows=260
            )
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
            extracted_data = pd.read_csv(f"CSV_FILES/CFTC_{selected_asset}.csv")
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


if __name__ == "__main__":
    app.run_server(debug=True)

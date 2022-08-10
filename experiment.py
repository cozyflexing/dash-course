import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import data_calculations as dcalc

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
    "Net Position",
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
]

app = dash.Dash()

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1("Sixteen Analytics Dashboard"),
                html.H1("Regular Charts"),
                dcc.Dropdown(id="asset_options", options=asset_options, value="USD"),
            ]
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id="data_options", options=data_options, value="Open Interest"
                ),
                dcc.Dropdown(id="lookback", options=look_back_options, value="1 Year"),
                dcc.Graph(id="regular_data_graph"),
                html.Div(id="average_data_calc"),
            ]
        ),
        html.Div(
            [
                html.H1("Calculation Charts"),
                dcc.Dropdown(
                    id="asset_options_calc", options=asset_options, value="NASDAQ"
                ),
                dcc.Dropdown(
                    id="calc_options",
                    options=calc_options,
                    value="COT Index Commercial",
                ),
                dcc.Dropdown(
                    id="lookback_calc", options=look_back_options, value="1 Year"
                ),
                dcc.Graph(id="calculated_data_garph"),
            ]
        ),
    ]
)


@app.callback(
    Output(component_id="regular_data_graph", component_property="figure"),
    Output(component_id="average_data_calc", component_property="children"),
    Input(component_id="asset_options", component_property="value"),
    Input(component_id="data_options", component_property="value"),
    Input(component_id="lookback", component_property="value"),
)
def standard_graph_update(selected_asset, selected_data, selected_lookback):
    if selected_lookback == "6 Months":
        extracted_data = pd.read_csv(f"CSV FILES/CFTC_{selected_asset}.csv", nrows=26)
        line_fig = px.line(
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
        selected_average = extracted_data[f"{selected_data}"].mean()
    elif selected_lookback == "1 Year":
        extracted_data = pd.read_csv(f"CSV FILES/CFTC_{selected_asset}.csv", nrows=52)
        line_fig = px.line(
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
        selected_average = extracted_data[f"{selected_data}"].mean()
    elif selected_lookback == "3 Years":
        extracted_data = pd.read_csv(f"CSV FILES/CFTC_{selected_asset}.csv", nrows=156)
        line_fig = px.line(
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
        selected_average = extracted_data[f"{selected_data}"].mean()
    elif selected_lookback == "5 Years":
        extracted_data = pd.read_csv(f"CSV FILES/CFTC_{selected_asset}.csv", nrows=260)
        line_fig = px.line(
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
        selected_average = extracted_data[f"{selected_data}"].mean()
    elif selected_lookback == "Max":
        extracted_data = pd.read_csv(f"CSV FILES/CFTC_{selected_asset}.csv")
        line_fig = px.line(
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data} {selected_asset}", "x": "Dates"},
        )
        selected_average = extracted_data[f"{selected_data}"].mean()
    return (
        line_fig,
        f"The average {selected_data} for {selected_asset} over {selected_lookback} is {selected_average}",
    )


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
                f"CSV FILES/CFTC_{selected_asset}.csv", nrows=26
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
                f"CSV FILES/CFTC_{selected_asset}.csv", nrows=52
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
                f"CSV FILES/CFTC_{selected_asset}.csv", nrows=156
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
                f"CSV FILES/CFTC_{selected_asset}.csv", nrows=260
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
            extracted_data = pd.read_csv(f"CSV FILES/CFTC_{selected_asset}.csv")
            for x in extracted_data["Commercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Commercial Net Position"].min(),
                        extracted_data["Commercial Net Position"].max(),
                    )
                )
        line_fig = px.line(
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
        if selected_lookback == "6 Months":
            extracted_data = pd.read_csv(
                f"CSV FILES/CFTC_{selected_asset}.csv", nrows=26
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
                f"CSV FILES/CFTC_{selected_asset}.csv", nrows=52
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
                f"CSV FILES/CFTC_{selected_asset}.csv", nrows=156
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
                f"CSV FILES/CFTC_{selected_asset}.csv", nrows=260
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
            extracted_data = pd.read_csv(f"CSV FILES/CFTC_{selected_asset}.csv")
            for x in extracted_data["Noncommercial Net Position"]:
                cot_index.append(
                    dcalc.cot_index_calculation(
                        x,
                        extracted_data["Noncommercial Net Position"].min(),
                        extracted_data["Noncommercial Net Position"].max(),
                    )
                )
        line_fig = px.line(
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
        line_fig = px.line()
        if selected_lookback == "6 Months":
            extracted_data = pd.read_csv(
                f"CSV FILES/CFTC_{selected_asset}.csv", nrows=26
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
                f"CSV FILES/CFTC_{selected_asset}.csv", nrows=52
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
                f"CSV FILES/CFTC_{selected_asset}.csv", nrows=156
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
                f"CSV FILES/CFTC_{selected_asset}.csv", nrows=260
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
            extracted_data = pd.read_csv(f"CSV FILES/CFTC_{selected_asset}.csv")
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
        line_fig = px.bar(x=extracted_data["Date"][6:], y=cot_movement_index)

    return line_fig


if __name__ == "__main__":
    app.run_server(debug=True)

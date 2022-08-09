import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import requests
import api_handling

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
]

asset_options = ["NASDAQ", "SP500", "GOLD"]

look_back_options = ["6 Months", "1 Year", "3 Years", "5 Years", "Max"]

app = dash.Dash()

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1("Sixteen Analytics Dashboard"),
                dcc.Dropdown(id="asset_options", options=asset_options, value="NASDAQ"),
            ]
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id="data_options", options=data_options, value="Open Interest"
                ),
                dcc.Dropdown(id="lookback", options=look_back_options, value="1 Year"),
                dcc.Graph(id="data_graph"),
                html.Div(id="average_oi"),
            ]
        ),
    ]
)


@app.callback(
    Output(component_id="data_graph", component_property="figure"),
    Output(component_id="average_oi", component_property="children"),
    Input(component_id="asset_options", component_property="value"),
    Input(component_id="data_options", component_property="value"),
    Input(component_id="lookback", component_property="value"),
)
def update_graph(selected_asset, selected_data, selected_lookback):
    if selected_lookback == "6 Months":
        extracted_data = pd.read_csv(f"CFTC_{selected_asset}.csv", nrows=26)
        line_fig = px.line(
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data}", "x": "Dates"},
        )
        selected_average = extracted_data[f"{selected_data}"].mean()
    elif selected_lookback == "1 Year":
        extracted_data = pd.read_csv(f"CFTC_{selected_asset}.csv", nrows=52)
        line_fig = px.line(
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data}", "x": "Dates"},
        )
        selected_average = extracted_data[f"{selected_data}"].mean()
    elif selected_lookback == "3 Years":
        extracted_data = pd.read_csv(f"CFTC_{selected_asset}.csv", nrows=156)
        line_fig = px.line(
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data}", "x": "Dates"},
        )
        selected_average = extracted_data[f"{selected_data}"].mean()
    elif selected_lookback == "5 Years":
        extracted_data = pd.read_csv(f"CFTC_{selected_asset}.csv", nrows=260)
        line_fig = px.line(
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data}", "x": "Dates"},
        )
        selected_average = extracted_data[f"{selected_data}"].mean()
    elif selected_lookback == "Max":
        extracted_data = pd.read_csv(f"CFTC_{selected_asset}.csv")
        line_fig = px.line(
            x=extracted_data["Date"],
            y=extracted_data[f"{selected_data}"],
            labels={"y": f"{selected_data}", "x": "Dates"},
        )
        selected_average = extracted_data[f"{selected_data}"].mean()
    return (
        line_fig,
        f"The average of {selected_data} for {selected_asset} over {selected_lookback} is {selected_average}",
    )


if __name__ == "__main__":
    app.run_server(debug=True)

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import requests

r = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/209742_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CFTC_NASDAQ.csv", "w+") as f:
    f.write(r.text)

nasdaq = pd.read_csv("CFTC_NASDAQ.csv")

look_back_options = ["6 Months", "1 Year", "3 Years", "5 Years", "Max"]

app = dash.Dash()

app.layout = html.Div(
    [
        html.H1("Sixteen Analytics Dashboard"),
        dcc.Dropdown(
            id="data_options", options=nasdaq.columns[1:], value="Open Interest"
        ),
        dcc.Dropdown(id="lookback", options=look_back_options, value="1 Year"),
        dcc.Graph(id="data_graph"),
    ]
)


@app.callback(
    Output(component_id="data_graph", component_property="figure"),
    Input(component_id="data_options", component_property="value"),
    Input(component_id="lookback", component_property="value"),
)
def update_graph(selected_date, selected_lookback):
    if selected_lookback == "6 Months":
        nasdaq = pd.read_csv("CFTC_NASDAQ.csv", nrows=26)
        line_fig = px.line(
            x=nasdaq["Date"],
            y=nasdaq[f"{selected_date}"],
            labels={"y": f"{selected_date}", "x": "Dates"},
        )
    elif selected_lookback == "1 Year":
        nasdaq = pd.read_csv("CFTC_NASDAQ.csv", nrows=52)
        line_fig = px.line(
            x=nasdaq["Date"],
            y=nasdaq[f"{selected_date}"],
            labels={"y": f"{selected_date}", "x": "Dates"},
        )
    elif selected_lookback == "3 Years":
        nasdaq = pd.read_csv("CFTC_NASDAQ.csv", nrows=156)
        line_fig = px.line(
            x=nasdaq["Date"],
            y=nasdaq[f"{selected_date}"],
            labels={"y": f"{selected_date}", "x": "Dates"},
        )
    elif selected_lookback == "5 Years":
        nasdaq = pd.read_csv("CFTC_NASDAQ.csv", nrows=260)
        line_fig = px.line(
            x=nasdaq["Date"],
            y=nasdaq[f"{selected_date}"],
            labels={"y": f"{selected_date}", "x": "Dates"},
        )
    elif selected_lookback == "Max":
        nasdaq = pd.read_csv("CFTC_NASDAQ.csv")
        line_fig = px.line(
            x=nasdaq["Date"],
            y=nasdaq[f"{selected_date}"],
            labels={"y": f"{selected_date}", "x": "Dates"},
        )
    return line_fig


if __name__ == "__main__":
    app.run_server(debug=True)

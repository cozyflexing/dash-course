import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

nasdaq = pd.read_csv("CFTC-209742_FO_L_ALL.csv")


app = dash.Dash()
value = "Open Interest"
app.layout = html.Div(
    [
        html.H1("NASDAQ Dashboard"),
        html.P(
            [
                "This dashboard shows NASDAQ info:",
                html.Br(),
                html.A(
                    "Nasdaq data scource",
                    href="https://data.nasdaq.com/data/CFTC/209742_FO_L_ALL-commitment-of-traders-nasdaq-mini-cme-futures-and-options-legacy-format-209742",
                    target="_blank",
                ),
            ]
        ),
        dcc.Dropdown(id="my_dropdown", options=nasdaq.columns, value="Open Interest"),
        dcc.Graph(id="my_graph"),
    ]
)


@app.callback(
    Output(component_id="my_graph", component_property="figure"),
    Input(component_id="my_dropdown", component_property="value"),
)
def update_graph(selected_value):
    line_fig = px.line(
        x=nasdaq["Date"],
        y=nasdaq[f"{selected_value}"],
        labels={"y": f"{selected_value}", "x": "Dates"},
    )
    return line_fig


if __name__ == "__main__":
    app.run_server(debug=True)

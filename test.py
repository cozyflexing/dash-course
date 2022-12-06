# # from pandas import to_datetime, read_sql
# # from listCreations import engine
# # from functions import total_open_interest


# # selectedColumn = "OpenInterest"

# # df = read_sql("CAD", engine)
# # df.Date = to_datetime(df.Date)

# # change = []

# # for x in range(0, 12):
# #     # change.append(abs(df.NoncommercialLong.iloc[0] - df.NoncommercialLong.iloc[x]))
# #     print(
# #         f"{df.Date.iloc[x]} - Net Noncomm: {(df.NoncommercialLong.iloc[x] - df.NoncommercialShort.iloc[x])} Noncomm diff longs: {(df.NoncommercialLong.iloc[0] - df.NoncommercialLong.iloc[x])} Noncomm diff shorts: {(df.NoncommercialShort.iloc[0] - df.NoncommercialShort.iloc[x])} Net Comm: {(df.CommercialLong.iloc[x] - df.CommercialShort.iloc[x])} Comm diff longs:{(df.CommercialLong.iloc[0] - df.CommercialLong.iloc[x])}  Comm diff shorts:{(df.CommercialShort.iloc[0] - df.CommercialShort.iloc[x])}\n"
# #     )


# # for x in range(0, 12):
# #     if change[x] == max(change):
# #         print(
# #             f"In the past {x} weeks the biggest change was {round((change[x]/(df.CommercialLong.iloc[x]+df.CommercialShort.iloc[x]))*100)}%"
# #         )

from dash import Dash, html, Input, Output, dash_table, dcc
import pandas as pd
from listCreations import engine
import functions
from dash_bootstrap_templates import load_figure_template
import dash_bootstrap_components as dbc


app = Dash(
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
    ]
)
load_figure_template("BOOTSTRAP")

df = pd.read_sql("CAD", engine)
df.Date = pd.to_datetime(df.Date)
df = pd.DataFrame(
    [
        [
            "Open Interest Commercial",
            (functions.total_open_interest_commercial(df.iloc[0])),
            functions.percentage_change(
                (functions.total_open_interest_commercial(df.iloc[0])),
                (functions.total_open_interest_commercial(df.iloc[11])),
            ),
            functions.percentage_change(
                (functions.total_open_interest_commercial(df.iloc[0])),
                (functions.total_open_interest_commercial(df.iloc[23])),
            ),
            functions.percentage_change(
                (functions.total_open_interest_commercial(df.iloc[0])),
                (functions.total_open_interest_commercial(df.iloc[51])),
            ),
        ],
        [
            "Open Interest Noncommercial",
            (functions.total_open_interest_noncommercial(df.iloc[0])),
            functions.percentage_change(
                (functions.total_open_interest_noncommercial(df.iloc[0])),
                (functions.total_open_interest_noncommercial(df.iloc[11])),
            ),
            functions.percentage_change(
                (functions.total_open_interest_noncommercial(df.iloc[0])),
                (functions.total_open_interest_noncommercial(df.iloc[23])),
            ),
            functions.percentage_change(
                (functions.total_open_interest_noncommercial(df.iloc[0])),
                (functions.total_open_interest_noncommercial(df.iloc[51])),
            ),
        ],
        [
            "Open Interest Nonreportable Positions",
            (functions.total_open_interest_nonreportable(df.iloc[0])),
            functions.percentage_change(
                (functions.total_open_interest_nonreportable(df.iloc[0])),
                (functions.total_open_interest_nonreportable(df.iloc[11])),
            ),
            functions.percentage_change(
                (functions.total_open_interest_nonreportable(df.iloc[0])),
                (functions.total_open_interest_nonreportable(df.iloc[23])),
            ),
            functions.percentage_change(
                (functions.total_open_interest_nonreportable(df.iloc[0])),
                (functions.total_open_interest_nonreportable(df.iloc[51])),
            ),
        ],
    ],
    columns=["Type", "Newest", "3 Month Change", "6 Month Change", "1 Year Change"],
)
app.layout = html.Div(
    children=[
        html.Div(id="my-input"),
        dbc.Row(
            [
                dbc.Col(html.P(id="type")),
                dbc.Col(html.P(id="3 Month")),
                dbc.Col(html.P(id="6 Month")),
                dbc.Col(html.P(id="1 Year")),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.P(id="my-output4")),
                dbc.Col(html.P(id="my-output5")),
                dbc.Col(html.P(id="my-output6")),
                dbc.Col(html.P(id="my-output6/5")),
            ]
        ),
        dbc.Row(
            [
                dbc.Col(html.P(id="my-output7")),
                dbc.Col(html.P(id="my-output8")),
                dbc.Col(html.P(id="my-output9")),
                dbc.Col(html.P(id="my-output9/5")),
            ]
        ),
    ]
)


@app.callback(
    Output(component_id="my-output4", component_property="children"),
    Output(component_id="my-output5", component_property="children"),
    Output(component_id="my-output6", component_property="children"),
    Output(component_id="my-output6/5", component_property="children"),
    Output(component_id="my-output7", component_property="children"),
    Output(component_id="my-output8", component_property="children"),
    Output(component_id="my-output9", component_property="children"),
    Output(component_id="my-output9/5", component_property="children"),
    Input(component_id="my-input", component_property="my-input"),
)
def update_output_div(input_value):
    df = pd.read_sql("CAD", engine)
    df.Date = pd.to_datetime(df.Date)
    result = functions.percentage_change(
        (functions.total_open_interest_noncommercial(df.iloc[0])),
        (functions.total_open_interest_noncommercial(df.iloc[11])),
    )
    return (
        f"{result}",
        f"{result}",
        f"{result}",
        f"{result}",
        f"{result}",
        f"{result}",
        f"{result}",
        f"{result}",
    )


if __name__ == "__main__":
    app.run_server(debug=True)

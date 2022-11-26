from dash import Dash, html, dcc, Input, Output
import sqlalchemy as sa
import pandas as pd
import plotly.express as px
from listCreations import columnOptions, tableOptions, engine

app = Dash()


app.layout = html.Div(
    children=[
        dcc.Dropdown(options=columnOptions, value="OpenInterest", id="columnDropdown"),
        dcc.Dropdown(options=tableOptions, value="EUR", id="tableDropdown"),
        html.Div(
            children=[
                dcc.Graph(id="renderedGraph"),
            ],
        ),
    ]
)


@app.callback(
    Output(component_id="renderedGraph", component_property="figure"),
    Input(component_id="columnDropdown", component_property="value"),
    Input(component_id="tableDropdown", component_property="value"),
)
def renderGraph(selectedColumn, selectedTable):
    df = pd.read_sql(selectedTable, engine)
    df.Date = pd.to_datetime(df.Date)
    lineFig = px.line(df, x=df.Date, y=selectedColumn, title=f"{selectedColumn}")
    return lineFig


if __name__ == "__main__":
    app.run_server(debug=True)

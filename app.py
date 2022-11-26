from dash import Dash, html, dcc, Input, Output
from pandas import to_datetime, read_sql
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from plotly.express import line
from listCreations import columnOptions, tableOptions, engine

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
load_figure_template("BOOTSTRAP")


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
    df = read_sql(selectedTable, engine)
    df.Date = to_datetime(df.Date)
    lineFig = line(df, x=df.Date, y=selectedColumn, title=f"{selectedColumn}")
    return lineFig


if __name__ == "__main__":
    app.run_server(debug=True)

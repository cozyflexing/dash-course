from dash import Dash, html, dcc, Input, Output
from pandas import to_datetime, read_sql
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from plotly.express import line
from listCreations import columnOptions, tableOptions, engine

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
load_figure_template("BOOTSTRAP")

GRID_STYLE = {
    "display": "grid",
    "height": "1000px",
    "grid-template-columns": "1fr 4fr",
    "grid-template-rows": "1fr",
    "grid-column-gap": "10px",
    "grid-row-gap": "10px",
}

SIDEBAR_STYLE = {
    "marginLeft": "10px",
    "marginTop": "10px",
    "height": "95%",
    "width": "95%",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-4"),
        html.Hr(),
        html.P("A simple sidebar layout with navigation links", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

app.layout = html.Div(
    children=[
        html.Div(
            children=[sidebar],
        ),
        html.Div(
            children=[
                dcc.Dropdown(
                    options=columnOptions, value="OpenInterest", id="columnDropdown"
                ),
                dcc.Dropdown(options=tableOptions, value="EUR", id="tableDropdown"),
                dcc.Graph(id="renderedGraph"),
            ],
        ),
    ],
    style=GRID_STYLE,
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

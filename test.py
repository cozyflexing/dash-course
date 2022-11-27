from dash import Dash, html, dcc, Input, Output
from pandas import to_datetime, read_sql
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from plotly.express import line
from listCreations import columnOptions, tableOptions, engine

selectedColumn = "OpenInterest"

df = read_sql("EUR", engine)
df.Date = to_datetime(df.Date)

print(df.Date.idxmin())

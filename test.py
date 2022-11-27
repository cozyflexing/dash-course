from dash import Dash, html, dcc, Input, Output
from pandas import to_datetime, read_sql
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from plotly.express import line
from listCreations import columnOptions, tableOptions, engine

selectedColumn = "OpenInterest"

df = read_sql("EUR", engine)
df.Date = to_datetime(df.Date)
mask = (df["Date"] > "2022-05-17") & (df["Date"] <= "2022-09-13")
df = df.loc[mask]
lineFig = line(df, x=df.Date, y=selectedColumn, title=f"{selectedColumn}")

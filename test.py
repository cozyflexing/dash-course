import sqlalchemy as sa
from sqlalchemy.schema import MetaData
import pandas as pd
import plotly.express as px


engine = sa.create_engine("sqlite:///sqlalchemyCFTCDATA.sqlite")
df = pd.read_sql("EUR", engine)
df.Date = pd.to_datetime(df.Date)

fig = px.line(df, df.Date, df.TotalShort)
optionList = []

meta = MetaData()
meta.reflect(bind=engine)

tables = meta.tables.keys()

for x in tables:
    print(x)

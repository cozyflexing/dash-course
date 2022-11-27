from sqlalchemy.schema import MetaData
import sqlalchemy as sa
import pandas as pd


engine = sa.create_engine("sqlite:///sqlalchemyCFTCDATA.sqlite")
df = pd.read_sql("EUR", engine)
df.Date = pd.to_datetime(df.Date)
meta = MetaData()
meta.reflect(bind=engine)

columnOptions, tableOptions = [], []

tables = meta.tables.keys()


for table in tables:
    tableOptions.append(table)
for col in df.head():
    columnOptions.append(col)

columnOptions.remove("Date")

import sqlalchemy as sa
import pandas as pd


engine = sa.create_engine("sqlite:///sqlalchemyCFTCDATA.sqlite")
df = pd.read_sql("EUR", engine)
df.Date = pd.to_datetime(df.Date)

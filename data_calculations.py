import pandas as pd
import plotly.express as px

NASDAQ_data = pd.read_csv(f"CSV FILES/CFTC_NASDAQ.csv")

cot_index = []


def cot_index_calculation(x, y, z):
    cotindex = 100 * (x - y) / (z - y)
    return cotindex


for x in NASDAQ_data["Net Position"]:
    cot_index.append(
        cot_index_calculation(
            x,
            NASDAQ_data["Net Position"].min(),
            NASDAQ_data["Net Position"].max(),
        )
    )

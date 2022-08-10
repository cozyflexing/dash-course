import pandas as pd
import plotly.express as px

NASDAQ_data = pd.read_csv(f"CSV FILES/CFTC_NASDAQ.csv", nrows=52)

cot_index = []
copy_of_cot_index = []
cot_movement_index = []


def cot_index_calculation(x, y, z):
    cotindex = 100 * (x - y) / (z - y)
    return cotindex


for x in NASDAQ_data["Commercial Net Position"]:
    cot_index.append(
        cot_index_calculation(
            x,
            NASDAQ_data["Commercial Net Position"].min(),
            NASDAQ_data["Commercial Net Position"].max(),
        )
    )

for x in cot_index:
    copy_of_cot_index.append(x)
    if len(copy_of_cot_index) >= 7:
        difference = copy_of_cot_index[-7] - copy_of_cot_index[-1]
        cot_movement_index.append(difference)
    

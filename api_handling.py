import pandas as pd
import requests

nasdaq_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/209742_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CFTC_NASDAQ.csv", "w+") as f:
    f.write(nasdaq_response.text)

sp_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/13874A_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CFTC_SP500.csv", "w+") as f:
    f.write(sp_response.text)

gold_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/088691_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CFTC_GOLD.csv", "w+") as f:
    f.write(gold_response.text)

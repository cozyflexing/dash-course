import pandas as pd
import requests

NASDAQ_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/209742_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_NASDAQ.csv", "w+") as f:
    f.write(NASDAQ_response.text)

SP500_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/13874A_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_SP500.csv", "w+") as f:
    f.write(SP500_response.text)

GOLD_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/088691_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_GOLD.csv", "w+") as f:
    f.write(GOLD_response.text)

SILVER_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/084691_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_SILVER.csv", "w+") as f:
    f.write(SILVER_response.text)

EURO_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/096742_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_EURO.csv", "w+") as f:
    f.write(EURO_response.text)

USD_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/098662_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_USD.csv", "w+") as f:
    f.write(USD_response.text)

GBP_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/096742_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_GBP.csv", "w+") as f:
    f.write(GBP_response.text)

CAD_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/090741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_CAD.csv", "w+") as f:
    f.write(CAD_response.text)

JPY_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/097741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_JPY.csv", "w+") as f:
    f.write(JPY_response.text)

AUD_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/232741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_AUD.csv", "w+") as f:
    f.write(AUD_response.text)

NZD_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/112741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_NZD.csv", "w+") as f:
    f.write(NZD_response.text)

CHF_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/092741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_CHF.csv", "w+") as f:
    f.write(CHF_response.text)

WTI_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/067651_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_WTI.csv", "w+") as f:
    f.write(WTI_response.text)

import pandas as pd
import requests
import time

start = time.time()

NASDAQ_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/209742_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_NASDAQ.csv", "w+") as f:
    f.write(NASDAQ_response.text)

NASDAQ_data = pd.read_csv(f"CSV FILES/CFTC_NASDAQ.csv")

NASDAQ_data["Commercial Net Position"] = (
    NASDAQ_data["Commercial Long"] - NASDAQ_data["Commercial Short"]
)
NASDAQ_data["Noncommercial Net Position"] = (
    NASDAQ_data["Noncommercial Long"] - NASDAQ_data["Noncommercial Short"]
)

NASDAQ_data_csv = NASDAQ_data.to_csv(
    path_or_buf="CSV FILES/CFTC_NASDAQ.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)


SP500_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/13874A_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_SP500.csv", "w+") as f:
    f.write(SP500_response.text)

SP500_data = pd.read_csv(f"CSV FILES/CFTC_SP500.csv")

SP500_data["Commercial Net Position"] = (
    SP500_data["Commercial Long"] - SP500_data["Commercial Short"]
)
SP500_data["Noncommercial Net Position"] = (
    SP500_data["Noncommercial Long"] - SP500_data["Noncommercial Short"]
)

SP500_data_csv = SP500_data.to_csv(
    path_or_buf="CSV FILES/CFTC_SP500.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)

GOLD_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/088691_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_GOLD.csv", "w+") as f:
    f.write(GOLD_response.text)

GOLD_data = pd.read_csv(f"CSV FILES/CFTC_GOLD.csv")

GOLD_data["Commercial Net Position"] = (
    GOLD_data["Commercial Long"] - GOLD_data["Commercial Short"]
)
GOLD_data["Noncommercial Net Position"] = (
    GOLD_data["Noncommercial Long"] - GOLD_data["Noncommercial Short"]
)

GOLD_data_csv = GOLD_data.to_csv(
    path_or_buf="CSV FILES/CFTC_GOLD.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)

SILVER_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/084691_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_SILVER.csv", "w+") as f:
    f.write(SILVER_response.text)

SILVER_data = pd.read_csv(f"CSV FILES/CFTC_SILVER.csv")

SILVER_data["Commercial Net Position"] = (
    SILVER_data["Commercial Long"] - SILVER_data["Commercial Short"]
)
SILVER_data["Noncommercial Net Position"] = (
    SILVER_data["Noncommercial Long"] - SILVER_data["Noncommercial Short"]
)

SILVER_data_csv = SILVER_data.to_csv(
    path_or_buf="CSV FILES/CFTC_SILVER.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)

EURO_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/096742_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_EURO.csv", "w+") as f:
    f.write(EURO_response.text)

EURO_data = pd.read_csv(f"CSV FILES/CFTC_EURO.csv")

EURO_data["Commercial Net Position"] = (
    EURO_data["Commercial Long"] - EURO_data["Commercial Short"]
)
EURO_data["Noncommercial Net Position"] = (
    EURO_data["Noncommercial Long"] - EURO_data["Noncommercial Short"]
)

EURO_data_csv = EURO_data.to_csv(
    path_or_buf="CSV FILES/CFTC_EURO.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)

USD_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/098662_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_USD.csv", "w+") as f:
    f.write(USD_response.text)

USD_data = pd.read_csv(f"CSV FILES/CFTC_USD.csv")

USD_data["Commercial Net Position"] = (
    USD_data["Commercial Long"] - USD_data["Commercial Short"]
)
USD_data["Noncommercial Net Position"] = (
    USD_data["Noncommercial Long"] - USD_data["Noncommercial Short"]
)

USD_data_csv = USD_data.to_csv(
    path_or_buf="CSV FILES/CFTC_USD.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)

GBP_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/096742_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_GBP.csv", "w+") as f:
    f.write(GBP_response.text)

GBP_data = pd.read_csv(f"CSV FILES/CFTC_GBP.csv")

GBP_data["Commercial Net Position"] = (
    GBP_data["Commercial Long"] - GBP_data["Commercial Short"]
)
GBP_data["Noncommercial Net Position"] = (
    GBP_data["Noncommercial Long"] - GBP_data["Noncommercial Short"]
)

GBP_data_csv = GBP_data.to_csv(
    path_or_buf="CSV FILES/CFTC_GBP.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)

CAD_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/090741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_CAD.csv", "w+") as f:
    f.write(CAD_response.text)

CAD_data = pd.read_csv(f"CSV FILES/CFTC_CAD.csv")

CAD_data["Commercial Net Position"] = (
    CAD_data["Commercial Long"] - CAD_data["Commercial Short"]
)
CAD_data["Noncommercial Net Position"] = (
    CAD_data["Noncommercial Long"] - CAD_data["Noncommercial Short"]
)

CAD_data_csv = CAD_data.to_csv(
    path_or_buf="CSV FILES/CFTC_CAD.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)

JPY_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/097741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_JPY.csv", "w+") as f:
    f.write(JPY_response.text)

JPY_data = pd.read_csv(f"CSV FILES/CFTC_JPY.csv")

JPY_data["Commercial Net Position"] = (
    JPY_data["Commercial Long"] - JPY_data["Commercial Short"]
)
JPY_data["Noncommercial Net Position"] = (
    JPY_data["Noncommercial Long"] - JPY_data["Noncommercial Short"]
)

JPY_data_csv = JPY_data.to_csv(
    path_or_buf="CSV FILES/CFTC_JPY.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)

AUD_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/232741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_AUD.csv", "w+") as f:
    f.write(AUD_response.text)

AUD_data = pd.read_csv(f"CSV FILES/CFTC_AUD.csv")

AUD_data["Commercial Net Position"] = (
    AUD_data["Commercial Long"] - AUD_data["Commercial Short"]
)
AUD_data["Noncommercial Net Position"] = (
    AUD_data["Noncommercial Long"] - AUD_data["Noncommercial Short"]
)

AUD_data_csv = AUD_data.to_csv(
    path_or_buf="CSV FILES/CFTC_AUD.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)

NZD_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/112741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_NZD.csv", "w+") as f:
    f.write(NZD_response.text)

NZD_data = pd.read_csv(f"CSV FILES/CFTC_NZD.csv")

NZD_data["Commercial Net Position"] = (
    NZD_data["Commercial Long"] - NZD_data["Commercial Short"]
)
NZD_data["Noncommercial Net Position"] = (
    NZD_data["Noncommercial Long"] - NZD_data["Noncommercial Short"]
)

NZD_data_csv = NZD_data.to_csv(
    path_or_buf="CSV FILES/CFTC_NZD.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)

CHF_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/092741_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_CHF.csv", "w+") as f:
    f.write(CHF_response.text)

CHF_data = pd.read_csv(f"CSV FILES/CFTC_CHF.csv")

CHF_data["Commercial Net Position"] = (
    CHF_data["Commercial Long"] - CHF_data["Commercial Short"]
)
CHF_data["Noncommercial Net Position"] = (
    CHF_data["Noncommercial Long"] - CHF_data["Noncommercial Short"]
)

CHF_data_csv = CHF_data.to_csv(
    path_or_buf="CSV FILES/CFTC_CHF.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)

WTI_response = requests.get(
    "https://data.nasdaq.com/api/v3/datasets/CFTC/067651_FO_L_ALL.csv?api_key=dKxFC2Wn7ckKFyatyDC3"
)

with open("CSV FILES/CFTC_WTI.csv", "w+") as f:
    f.write(WTI_response.text)

WTI_data = pd.read_csv(f"CSV FILES/CFTC_WTI.csv")

WTI_data["Commercial Net Position"] = (
    WTI_data["Commercial Long"] - WTI_data["Commercial Short"]
)
WTI_data["Noncommercial Net Position"] = (
    WTI_data["Noncommercial Long"] - WTI_data["Noncommercial Short"]
)

WTI_data_csv = WTI_data.to_csv(
    path_or_buf="CSV FILES/CFTC_WTI.csv",
    sep=",",
    columns=[
        "Date",
        "Open Interest",
        "Noncommercial Long",
        "Noncommercial Short",
        "Noncommercial Spreads",
        "Commercial Long",
        "Commercial Short",
        "Total Long",
        "Total Short",
        "Nonreportable Positions Long",
        "Nonreportable Positions Short",
        "Commercial Net Position",
        "Noncommercial Net Position",
    ],
    header=True,
    index=True,
    encoding=None,
    compression="infer",
    date_format=None,
)

end = time.time()

print("The time of execution of above program is :", end - start)

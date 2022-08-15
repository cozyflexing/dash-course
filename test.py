import pandas as pd

extracted_data = pd.read_csv(f"CSV_FILES/CFTC_USD.csv", nrows=1)

noncommercial_percentage_of_total_oi = (
    extracted_data["Noncommercial Net Position"] / extracted_data["Open Interest"]
) * 100

commercial_percentage_of_total_oi = (
    extracted_data["Commercial Net Position"] / extracted_data["Open Interest"]
) * 100

short_percentage_of_noncommercial_oi = (
    extracted_data["Noncommercial Short"] / extracted_data["Noncommercial Long"]
    + extracted_data["Noncommercial Short"] * 100
)

short_percentage_of_commercial_oi = (
    extracted_data["Commercial Short"] / extracted_data["Commercial Long"]
    + extracted_data["Commercial Short"] * 100
)

long_percentage_of_commercial_oi = (
    extracted_data["Commercial Long"] / extracted_data["Commercial Long"]
    + extracted_data["Commercial Short"] * 100
)

long_percentage_of_noncommercial_oi = (
    extracted_data["Noncommercial Long"] / extracted_data["Noncommercial Long"]
    + extracted_data["Noncommercial Short"] * 100
)

short_percentage_of_total_oi = (
    extracted_data["Total Short"] / extracted_data["Open Interest"] * 100
)

long_percentage_of_total_oi = (
    extracted_data["Total Long"] / extracted_data["Open Interest"] * 100
)

########
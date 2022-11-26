from datetime import date
from dash import Dash, dcc, html
from listCreations import engine
from dash.dependencies import Input, Output
from pandas import read_sql

app = Dash(__name__)

df = read_sql("EUR", engine)


app.layout = html.Div(
    [
        dcc.DatePickerRange(
            id="my-date-picker-range",
            min_date_allowed=date(2000, 1, 1),
            max_date_allowed=date.today(),
            initial_visible_month=date.today(),
            end_date=date.today(),
        ),
        html.Div(id="output-container-date-picker-range"),
    ]
)


@app.callback(
    Output("output-container-date-picker-range", "children"),
    Input("my-date-picker-range", "start_date"),
    Input("my-date-picker-range", "end_date"),
)
def update_output(start_date, end_date):
    string_prefix = "You have selected: "
    if start_date is not None:
        start_date_object = date.fromisoformat(start_date)
        start_date_string = start_date_object.strftime("%D")
        string_prefix = string_prefix + "Start Date: " + start_date_string + " - "
    if end_date is not None:
        end_date_object = date.fromisoformat(end_date)
        end_date_string = end_date_object.strftime("%B %d, %Y")
        string_prefix = string_prefix + "End Date: " + end_date_string
    if len(string_prefix) == len("You have selected: "):
        return "Select a date to see it displayed here"
    else:
        return (string_prefix,)


if __name__ == "__main__":
    app.run_server(debug=True)

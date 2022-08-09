import pandas as pd
import plotly.express as px

def cot_index_calculation(x, y, z):
    cotindex = 100 * (x - y) / (z - y)
    return cotindex
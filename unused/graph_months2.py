from convert_data import time_data
from pandas import to_datetime as date
import plotly
import plotly.graph_objs as go

df = time_data(2812)
rows = len(df.index)

months = ['march', 'april', 'may', 'june', 'september', 'october', 'november']
march_long_sum, march_middle_sum, march_sprint_sum = 0, 0, 0
april_long_sum, april_middle_sum, april_sprint_sum = 0, 0, 0
may_long_sum, may_middle_sum, may_sprint_sum = 0, 0, 0
june_long_sum, june_middle_sum, june_sprint_sum = 0, 0, 0
july_long_sum, july_middle_sum, july_sprint_sum = 0, 0, 0
august_long_sum, august_middle_sum, august_sprint_sum = 0, 0, 0
september_long_sum, september_middle_sum, september_sprint_sum = 0, 0, 0
october_long_sum, october_middle_sum, october_sprint_sum = 0, 0, 0
november_long_sum, november_middle_sum, november_sprint_sum = 0, 0, 0

for i in range (rows):
    if df["date"][i] == 3:
        if df["discipline"][i] == 1:
            march_long_sum += df["time_min"][i]
        elif df["discipline"][i] == 2:
            march_middle_sum += df["time_min"][i]
        elif df["discipline"][i] == 3:
            march_sprint_sum += df["time_min"][i]
    if df["date"][i] == 4:
        if df["discipline"][i] == 1:
            april_long_sum += df["time_min"][i]
        elif df["discipline"][i] == 2:
            april_middle_sum += df["time_min"][i]
        elif df["discipline"][i] ==3:
            april_sprint_sum += df["time_min"][i]
    elif df["date"][i] == 5:
        if df["discipline"][i] == 1:
            may_long_sum += df["time_min"][i]
        elif df["discipline"][i] == 2:
            may_middle_sum += df["time_min"][i]
        elif df["discipline"][i] ==3:
            may_sprint_sum += df["time_min"][i]
    elif df["date"][i] == 6:
        if df["discipline"][i] == 1:
            june_long_sum += df["time_min"][i]
        elif df["discipline"][i] == 2:
            june_middle_sum += df["time_min"][i]
        elif df["discipline"][i] ==3:
            june_sprint_sum += df["time_min"][i]
    elif df["date"][i] == 7:
        if df["discipline"][i] == 1:
            july_long_sum += df["time_min"][i]
        elif df["discipline"][i] == 2:
            july_middle_sum += df["time_min"][i]
        elif df["discipline"][i] ==3:
            july_sprint_sum += df["time_min"][i]
    elif df["date"][i] == 8:
        if df["discipline"][i] == 1:
            august_long_sum += df["time_min"][i]
        elif df["discipline"][i] == 2:
            august_middle_sum += df["time_min"][i]
        elif df["discipline"][i] ==3:
            august_sprint_sum += df["time_min"][i]
    elif df["date"][i] == 9:
        if df["discipline"][i] == 1:
            september_long_sum += df["time_min"][i]
        elif df["discipline"][i] == 2:
            september_middle_sum += df["time_min"][i]
        elif df["discipline"][i] ==3:
            september_sprint_sum += df["time_min"][i]
    elif df["date"][i] == 10:
        if df["discipline"][i] == 1:
            october_long_sum += df["time_min"][i]
        elif df["discipline"][i] == 2:
            october_middle_sum += df["time_min"][i]
        elif df["discipline"][i] ==3:
            october_sprint_sum += df["time_min"][i]
    elif df["date"][i] == 11:
        if df["discipline"][i] == 1:
            november_long_sum += df["time_min"][i]
        elif df["discipline"][i] == 2:
            november_middle_sum += df["time_min"][i]
        elif df["discipline"][i] ==3:
            november_sprint_sum += df["time_min"][i]

# stacked bar graph
trace1 = go.Bar(x = months,
y=[march_long_sum, april_long_sum, may_long_sum, june_long_sum,
   september_long_sum, october_long_sum, november_long_sum],
name='klasika'
)
trace2 = go.Bar(
x= months,
y=[march_middle_sum, april_middle_sum, may_middle_sum, june_middle_sum,
   september_middle_sum, october_middle_sum, november_middle_sum],
name='middle'
)
trace3 = go.Bar(
x= months,
y=[march_sprint_sum, april_sprint_sum, may_sprint_sum, june_sprint_sum,
   september_sprint_sum, october_sprint_sum, november_sprint_sum],
name='sprint'
)
data = [trace1, trace2, trace3]
layout = go.Layout(
barmode='stack',
title='Naběhaný čas za jednotlivé měsíce'
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='time_months_stacked.html')
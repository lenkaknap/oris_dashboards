from convert_data import kilometers_data

from pandas import to_datetime as date
import plotly

import plotly.graph_objs as go

df = kilometers_data(3483)
print(df)
rows = len(df.index)

df["date"] = date(df["date"]).dt.month # move to convert_data function???
print(df)

months = ['january', 'february', 'march', 'april', 'may', 'june', 'september', 'october', 'november']
# values = {
# 'march':0,
# 'april', 'may', 'june', 'september', 'october', 'november'
# }

march_long_sum, march_middle_sum, march_sprint_sum = 0, 0, 0
april_long_sum, april_middle_sum, april_sprint_sum = 0, 0, 0
may_long_sum, may_middle_sum, may_sprint_sum = 0, 0, 0
june_long_sum, june_middle_sum, june_sprint_sum = 0, 0, 0
july_long_sum, july_middle_sum, july_sprint_sum = 0, 0, 0
august_long_sum, august_middle_sum, august_sprint_sum = 0, 0, 0
september_long_sum, september_middle_sum, september_sprint_sum = 0, 0, 0
october_long_sum, october_middle_sum, october_sprint_sum = 0, 0, 0
november_long_sum, november_middle_sum, november_sprint_sum = 0, 0, 0

#this is not working
for i in range (rows):
    month_num = df["date"][i]
    month = months[month_num-1]
    if df["discipline"][i] == 1:
        eval('{}_long_sum += df["distance"][i]'.format(month))
    elif df["discipline"][i] == 2:
        eval('{}_middle_sum += df["distance"][i]'.format(month))
    elif df["discipline"][i] == 3:
        eval('{}_sprint_sum += df["distance"][i]'.format(month))

trace1 = go.Bar(x= [months],
    y=[march_long_sum, april_long_sum, may_long_sum, june_long_sum, september_long_sum, october_long_sum, november_long_sum],
    name='long distance'
)
trace2 = go.Bar(
    x=[months],
    y=[march_middle_sum, april_middle_sum, may_middle_sum, june_middle_sum, september_middle_sum, october_middle_sum, november_middle_sum],
    name='middle distance'
)
trace3 = go.Bar(
    x=[months],
    y=[march_sprint_sum, april_sprint_sum, may_sprint_sum, june_sprint_sum, september_sprint_sum, october_sprint_sum, november_sprint_sum],
    name='sprint distance'
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='km_months_stacked2.html')
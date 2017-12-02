from convert_data import kilometers_data

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

#dat taky do funkci???
person_id = 3483
df = kilometers_data(person_id)
print(df)
rows = len(df.index)

# KILOMETERS
km_long_sum = 0
km_middle_sum = 0
km_sprint_sum = 0

for i in range (rows):
    if df["discipline"][i] == 1:
       km_long_sum += df["distance"][i]
    elif df["discipline"][i] == 2:
        km_middle_sum += df["distance"][i]
    elif df["discipline"][i] ==3:
        km_sprint_sum += df["distance"][i]
        
km_sum = []
km_sum.append(df["distance"].sum())
# controls_sum = df["controls"].sum()
# print("Nasel jsi {} kontrol".format(controls_sum))

print(km_long_sum)
print(km_middle_sum)
print(km_sprint_sum)
# print(km_sum)

# simple bar
data = [go.Bar(
            x=['km'],
            y= km_sum
    )]

plotly.offline.plot(data, filename='basic-bar.html')

# stacked bar graph
trace1 = go.Bar(x=['km'],
    y=[km_long_sum],
    name='long distance'
)
trace2 = go.Bar(
    x=['km'],
    y=[km_middle_sum],
    name='middle distance'
)
trace3 = go.Bar(
    x=['km'],
    y=[km_sprint_sum],
    name='sprint distance'
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='stacked-bar.html')

# CONTROLS
controls_long_sum = 0
controls_middle_sum = 0
controls_sprint_sum = 0

for i in range (rows):
    if df["discipline"][i] == 1:
       controls_long_sum += df["controls"][i]
    elif df["discipline"][i] == 2:
        controls_middle_sum += df["controls"][i]
    elif df["discipline"][i] ==3:
        controls_sprint_sum += df["controls"][i]
# stacked bar graph
trace1 = go.Bar(x=['controls'],
    y=[controls_long_sum],
    name='long distance'
)
trace2 = go.Bar(
    x=['controls'],
    y=[controls_middle_sum],
    name='middle distance'
)
trace3 = go.Bar(
    x=['controls'],
    y=[controls_sprint_sum],
    name='sprint distance'
)
data = [trace1, trace2, trace3]
layout = go.Layout(
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='D:\oris_files\oris\static\controls_stacked_bar.html')
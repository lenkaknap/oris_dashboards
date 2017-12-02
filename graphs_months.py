from convert_data import kilometers_data
import plotly
import plotly.graph_objs as go



def bar_graph_stacked_km(person_id):
    df = kilometers_data(person_id)
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
                march_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                march_middle_sum += df["distance"][i]
            elif df["discipline"][i] == 3:
                march_sprint_sum += df["distance"][i]
        if df["date"][i] == 4:
            if df["discipline"][i] == 1:
                april_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                april_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                april_sprint_sum += df["distance"][i]
        elif df["date"][i] == 5:
            if df["discipline"][i] == 1:
                may_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                may_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                may_sprint_sum += df["distance"][i]
        elif df["date"][i] == 6:
            if df["discipline"][i] == 1:
                june_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                june_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                june_sprint_sum += df["distance"][i]
        elif df["date"][i] == 7:
            if df["discipline"][i] == 1:
                july_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                july_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                july_sprint_sum += df["distance"][i]
        elif df["date"][i] == 8:
            if df["discipline"][i] == 1:
                august_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                august_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                august_sprint_sum += df["distance"][i]
        elif df["date"][i] == 9:
            if df["discipline"][i] == 1:
                september_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                september_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                september_sprint_sum += df["distance"][i]
        elif df["date"][i] == 10:
            if df["discipline"][i] == 1:
                october_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                october_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                october_sprint_sum += df["distance"][i]
        elif df["date"][i] == 11:
            if df["discipline"][i] == 1:
                november_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                november_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                november_sprint_sum += df["distance"][i]

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
    title='Počet kilometrů (vzdušnou čarou) za jednotlivé měsíce'
    )
    fig = go.Figure(data=data, layout=layout)
    return fig

def bar_graph_stacked_controls(person_id):
    df = kilometers_data(person_id)
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
                march_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                march_middle_sum += df["controls"][i]
            elif df["discipline"][i] == 3:
                march_sprint_sum += df["controls"][i]
        if df["date"][i] == 4:
            if df["discipline"][i] == 1:
                april_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                april_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                april_sprint_sum += df["controls"][i]
        elif df["date"][i] == 5:
            if df["discipline"][i] == 1:
                may_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                may_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                may_sprint_sum += df["controls"][i]
        elif df["date"][i] == 6:
            if df["discipline"][i] == 1:
                june_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                june_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                june_sprint_sum += df["controls"][i]
        elif df["date"][i] == 7:
            if df["discipline"][i] == 1:
                july_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                july_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                july_sprint_sum += df["controls"][i]
        elif df["date"][i] == 8:
            if df["discipline"][i] == 1:
                august_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                august_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                august_sprint_sum += df["controls"][i]
        elif df["date"][i] == 9:
            if df["discipline"][i] == 1:
                september_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                september_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                september_sprint_sum += df["controls"][i]
        elif df["date"][i] == 10:
            if df["discipline"][i] == 1:
                october_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                october_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                october_sprint_sum += df["controls"][i]
        elif df["date"][i] == 11:
            if df["discipline"][i] == 1:
                november_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                november_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                november_sprint_sum += df["controls"][i]

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
    title='Počet nalezených kontrol za jednotlivé měsíce'
    )
    fig = go.Figure(data=data, layout=layout)
    return fig

person_id = 3483
fig = bar_graph_stacked_km(person_id)
plotly.offline.plot(fig, filename='D:\oris_files\oris\static\km_months_stacked.html')
fig2 = bar_graph_stacked_controls(person_id)
plotly.offline.plot(fig2, filename='D:\oris_files\oris\static\controls_months_stacked.html')

# print(bar_graph_stacked_km(person_id)[0])
# print(bar_graph_stacked_km(person_id)[1])
#
# fig = go.Figure(bar_graph_stacked_km(person_id)[0], bar_graph_stacked_km(person_id)[1])

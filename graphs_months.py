from convert_data import kilometers_data, time_data
import plotly
import plotly.graph_objs as go


def bar_graph_stacked_km(person_id):
    df = kilometers_data(person_id)
    rows = len(df.index)

    months = ['březen', 'duben', 'květen', 'červen', 'září', 'říjen', 'listopad']
    march_long_sum, march_middle_sum, march_sprint_sum = 0, 0, 0
    april_long_sum, april_middle_sum, april_sprint_sum = 0, 0, 0
    may_long_sum, may_middle_sum, may_sprint_sum = 0, 0, 0
    june_long_sum, june_middle_sum, june_sprint_sum = 0, 0, 0
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
    name='klasika',
    opacity=0.9
    )
    trace2 = go.Bar(
    x= months,
    y=[march_middle_sum, april_middle_sum, may_middle_sum, june_middle_sum,
       september_middle_sum, october_middle_sum, november_middle_sum],
    name='middle',
    opacity=0.9
    )
    trace3 = go.Bar(
    x= months,
    y=[march_sprint_sum, april_sprint_sum, may_sprint_sum, june_sprint_sum,
       september_sprint_sum, october_sprint_sum, november_sprint_sum],
    name='sprint',
    opacity=0.9
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(
    barmode='stack',
    title='KILOMETRY naběhané za jednotlivé měsíce',
    font=dict(family='sans-serif')
    )

    fig = go.Figure(data=data, layout=layout)
    fig_plot = plotly.offline.plot(fig, output_type='div')
    return fig_plot

def bar_graph_stacked_controls(person_id):
    df = kilometers_data(person_id)
    rows = len(df.index)

    months = ['březen', 'duben', 'květen', 'červen', 'září', 'říjen', 'listopad']
    march_long_sum, march_middle_sum, march_sprint_sum = 0, 0, 0
    april_long_sum, april_middle_sum, april_sprint_sum = 0, 0, 0
    may_long_sum, may_middle_sum, may_sprint_sum = 0, 0, 0
    june_long_sum, june_middle_sum, june_sprint_sum = 0, 0, 0
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
    name='klasika',
    opacity=0.9
    )
    trace2 = go.Bar(
    x= months,
    y=[march_middle_sum, april_middle_sum, may_middle_sum, june_middle_sum,
       september_middle_sum, october_middle_sum, november_middle_sum],
    name='middle',
    opacity=0.9
    )
    trace3 = go.Bar(
    x= months,
    y=[march_sprint_sum, april_sprint_sum, may_sprint_sum, june_sprint_sum,
       september_sprint_sum, october_sprint_sum, november_sprint_sum],
    name='sprint',
    opacity=0.9
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(
    barmode='stack',
    title='KONTROLY nalezené za jednotlivé měsíce',
    font=dict(family='sans-serif')
    )

    fig = go.Figure(data=data, layout=layout)
    fig_plot = plotly.offline.plot(fig, output_type='div')
    return fig_plot

def bar_graph_stacked_time(person_id):
    df = time_data(person_id)
    rows = len(df.index)

    months = ['březen', 'duben', 'květen', 'červen', 'září', 'říjen', 'listopad']
    march_long_sum, march_middle_sum, march_sprint_sum = 0, 0, 0
    april_long_sum, april_middle_sum, april_sprint_sum = 0, 0, 0
    may_long_sum, may_middle_sum, may_sprint_sum = 0, 0, 0
    june_long_sum, june_middle_sum, june_sprint_sum = 0, 0, 0
    september_long_sum, september_middle_sum, september_sprint_sum = 0, 0, 0
    october_long_sum, october_middle_sum, october_sprint_sum = 0, 0, 0
    november_long_sum, november_middle_sum, november_sprint_sum = 0, 0, 0

    for i in range(rows):
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
            elif df["discipline"][i] == 3:
                april_sprint_sum += df["time_min"][i]
        elif df["date"][i] == 5:
            if df["discipline"][i] == 1:
                may_long_sum += df["time_min"][i]
            elif df["discipline"][i] == 2:
                may_middle_sum += df["time_min"][i]
            elif df["discipline"][i] == 3:
                may_sprint_sum += df["time_min"][i]
        elif df["date"][i] == 6:
            if df["discipline"][i] == 1:
                june_long_sum += df["time_min"][i]
            elif df["discipline"][i] == 2:
                june_middle_sum += df["time_min"][i]
            elif df["discipline"][i] == 3:
                june_sprint_sum += df["time_min"][i]
        elif df["date"][i] == 9:
            if df["discipline"][i] == 1:
                september_long_sum += df["time_min"][i]
            elif df["discipline"][i] == 2:
                september_middle_sum += df["time_min"][i]
            elif df["discipline"][i] == 3:
                september_sprint_sum += df["time_min"][i]
        elif df["date"][i] == 10:
            if df["discipline"][i] == 1:
                october_long_sum += df["time_min"][i]
            elif df["discipline"][i] == 2:
                october_middle_sum += df["time_min"][i]
            elif df["discipline"][i] == 3:
                october_sprint_sum += df["time_min"][i]
        elif df["date"][i] == 11:
            if df["discipline"][i] == 1:
                november_long_sum += df["time_min"][i]
            elif df["discipline"][i] == 2:
                november_middle_sum += df["time_min"][i]
            elif df["discipline"][i] == 3:
                november_sprint_sum += df["time_min"][i]

    # stacked bar graph
    trace1 = go.Bar(
        x=months,
        y=[march_long_sum, april_long_sum, may_long_sum, june_long_sum,
           september_long_sum, october_long_sum, november_long_sum],
        name='klasika',
        opacity=0.9
    )
    trace2 = go.Bar(
        x=months,
        y=[march_middle_sum, april_middle_sum, may_middle_sum, june_middle_sum,
           september_middle_sum, october_middle_sum, november_middle_sum],
        name='middle',
        opacity=0.9
    )
    trace3 = go.Bar(
        x=months,
        y=[march_sprint_sum, april_sprint_sum, may_sprint_sum, june_sprint_sum,
           september_sprint_sum, october_sprint_sum, november_sprint_sum],
        name='sprint',
        opacity=0.9
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(
        barmode='stack',
        title='ČAS (v minutách) naběhaný za jednotlivé měsíce',
        font=dict(family='sans-serif')
    )
    fig = go.Figure(data=data, layout=layout)
    fig_plot = plotly.offline.plot(fig, output_type='div')
    return fig_plot


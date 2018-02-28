import plotly
import plotly.graph_objs as go


def text_info(data_frame):
    df = data_frame
    rows = len(df.index)

    sum_time_hr = str(round(df['time_min'].sum() / 60, 2))

    sum_km = 0
    for i in range (rows):
        if df['time_min'][i] == 0:
            continue
        else:
            sum_km += df['distance'][i]
    sum_km = str(round(sum_km, 2))

    sum_controls = 0
    for i in range(rows):
        if df['time_min'][i] == 0:
            continue
        else:
            sum_controls += df['controls'][i]
    sum_controls = str(round(sum_controls, 2))

    # lists for paces in specific disciplines
    pace_long = []
    pace_middle = []
    pace_sprint = []

    for i in range(rows):
        if df['time_min'][i] == 0 or df['distance'][i] == 0:
            continue
        pace = df['time_min'][i] / df['distance'][i]
        if df['discipline'][i] == 1:
            pace_long.append(pace)
        elif df['discipline'][i] == 2:
            pace_middle.append(pace)
        elif df['discipline'][i] == 3:
            pace_sprint.append(pace)

    if len(pace_long) == 0:
        pace_long_mean, pace_long_min, pace_long_max = 0, 0, 0
    else:
        pace_long_mean = str(round(sum(pace_long) / len(pace_long), 2))
        pace_long_min = str(round(min(pace_long), 2))
        pace_long_max = str(round(max(pace_long), 2))

    if len(pace_middle) == 0:
        pace_middle_mean, pace_middle_min, pace_middle_max = 0, 0, 0
    else:
        pace_middle_mean = str(round(sum(pace_middle) / len(pace_middle), 2))
        pace_middle_min = str(round(min(pace_middle), 2))
        pace_middle_max = str(round(max(pace_middle), 2))

    if len(pace_sprint) == 0:
        pace_sprint_mean, pace_sprint_min, pace_sprint_max = 0, 0, 0
    else:
        pace_sprint_mean = str(round(sum(pace_sprint) / len(pace_sprint), 2))
        pace_sprint_min = str(round(min(pace_sprint), 2))
        pace_sprint_max = str(round(max(pace_sprint), 2))

    # list to put the values in
    statistics = []
    statistics.extend((sum_time_hr, sum_km, sum_controls,
                       pace_long_mean, pace_long_min, pace_long_max,
                       pace_middle_mean, pace_middle_min, pace_middle_max,
                       pace_sprint_mean, pace_sprint_min, pace_sprint_max))
    return statistics


def map_scatter(data_frame):
    mapbox_access_token = 'pk.eyJ1IjoieDQwODQ5MSIsImEiOiJjamFjZXBxd2cwOTB0MzNxdTJsZDEybzNxIn0.bEA4K56yPb7ckl1npZgEEA'

    df = data_frame
    rows = len(df.index)
    latitude_ls = df['latitude'].tolist()
    longitude_ls = df['longitude'].tolist()
    name_date = []

    for i in range (rows):
        name_date.append(str(df['date'][i]) + '<br>' + str(df['classTxt'][i]) + '<br>' + str(df['name'][i]))

    data = go.Data([
        go.Scattermapbox(
            lat=latitude_ls,
            lon=longitude_ls,
            mode='markers',
            marker=go.Marker(
                size=12,
                color='rgb(0, 143, 149)'
            ),
            text= name_date,
        )
    ])
    layout = go.Layout(
        autosize=True,
        hovermode='y',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(lat=49.7745131, lon=15.4786125),
            pitch=0,
            zoom=6,
        ),
        font=dict(
            family='sans-serif',
            size=18,
        ),
        margin=go.Margin(
            l=0,
            r=0,
            b=0,
            t=0,
            pad=4
        )
    )
    fig = dict(data=data, layout=layout)
    fig_map = plotly.offline.plot(fig, output_type='div')
    return fig_map


def bar_graph_stacked_time(data_frame):
    df = data_frame
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
        if df["date_month"][i] == 3:
            if df["discipline"][i] == 1:
                march_long_sum += df["time_min"][i]
            elif df["discipline"][i] == 2:
                march_middle_sum += df["time_min"][i]
            elif df["discipline"][i] == 3:
                march_sprint_sum += df["time_min"][i]
        elif df["date_month"][i] == 4:
            if df["discipline"][i] == 1:
                april_long_sum += df["time_min"][i]
            elif df["discipline"][i] == 2:
                april_middle_sum += df["time_min"][i]
            elif df["discipline"][i] == 3:
                april_sprint_sum += df["time_min"][i]
        elif df["date_month"][i] == 5:
            if df["discipline"][i] == 1:
                may_long_sum += df["time_min"][i]
            elif df["discipline"][i] == 2:
                may_middle_sum += df["time_min"][i]
            elif df["discipline"][i] == 3:
                may_sprint_sum += df["time_min"][i]
        elif df["date_month"][i] == 6:
            if df["discipline"][i] == 1:
                june_long_sum += df["time_min"][i]
            elif df["discipline"][i] == 2:
                june_middle_sum += df["time_min"][i]
            elif df["discipline"][i] == 3:
                june_sprint_sum += df["time_min"][i]
        elif df["date_month"][i] == 9:
            if df["discipline"][i] == 1:
                september_long_sum += df["time_min"][i]
            elif df["discipline"][i] == 2:
                september_middle_sum += df["time_min"][i]
            elif df["discipline"][i] == 3:
                september_sprint_sum += df["time_min"][i]
        elif df["date_month"][i] == 10:
            if df["discipline"][i] == 1:
                october_long_sum += df["time_min"][i]
            elif df["discipline"][i] == 2:
                october_middle_sum += df["time_min"][i]
            elif df["discipline"][i] == 3:
                october_sprint_sum += df["time_min"][i]
        elif df["date_month"][i] == 11:
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
        marker=dict(
            color='rgb(0, 143, 149)'
        ),
        opacity=0.9
    )
    trace2 = go.Bar(
        x=months,
        y=[march_middle_sum, april_middle_sum, may_middle_sum, june_middle_sum,
           september_middle_sum, october_middle_sum, november_middle_sum],
        name='middle',
        marker=dict(
            color='rgb(226, 78, 66)'
        ),
        opacity=0.9
    )
    trace3 = go.Bar(
        x=months,
        y=[march_sprint_sum, april_sprint_sum, may_sprint_sum, june_sprint_sum,
           september_sprint_sum, october_sprint_sum, november_sprint_sum],
        name='sprint',
        marker=dict(
            color='rgb(233, 176, 0)'
        ),
        opacity=0.9
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(
        barmode='stack',
        yaxis=dict(
            title='minuty'
        ),
        font=dict(
            family='sans-serif',
            size=14
        ),
        margin=go.Margin(
            l=60,
            t=40,
            b=50,
            pad=4
        )
    )
    fig = go.Figure(data=data, layout=layout)
    fig_plot = plotly.offline.plot(fig, output_type='div')
    return fig_plot

def time_by_discipline(data_frame):
    df=data_frame
    rows = len(df.index)

    sum_time_long = 0
    sum_time_middle = 0
    sum_time_sprint = 0

    statistics=[]

    for i in range (rows):
        if df['discipline'][i] == 1:
            sum_time_long += df['time_min'][i]
        elif df['discipline'][i] == 2:
            sum_time_middle += df['time_min'][i]
        elif df['discipline'][i] == 3:
            sum_time_sprint += df['time_min'][i]

    sum_time_long = str(round(sum_time_long/60, 2))
    sum_time_middle = str(round(sum_time_middle/60, 2))
    sum_time_sprint = str(round(sum_time_sprint/60, 2))

    statistics.extend((sum_time_long, sum_time_middle, sum_time_sprint))
    return statistics


def bar_graph_stacked_km(data_frame):
    df = data_frame
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
        if df['time_min'][i] == 0:
            continue
        if df["date_month"][i] == 3:
            if df["discipline"][i] == 1:
                march_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                march_middle_sum += df["distance"][i]
            elif df["discipline"][i] == 3:
                march_sprint_sum += df["distance"][i]
        elif df["date_month"][i] == 4:
            if df["discipline"][i] == 1:
                april_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                april_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                april_sprint_sum += df["distance"][i]
        elif df["date_month"][i] == 5:
            if df["discipline"][i] == 1:
                may_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                may_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                may_sprint_sum += df["distance"][i]
        elif df["date_month"][i] == 6:
            if df["discipline"][i] == 1:
                june_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                june_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                june_sprint_sum += df["distance"][i]
        elif df["date_month"][i] == 9:
            if df["discipline"][i] == 1:
                september_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                september_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                september_sprint_sum += df["distance"][i]
        elif df["date_month"][i] == 10:
            if df["discipline"][i] == 1:
                october_long_sum += df["distance"][i]
            elif df["discipline"][i] == 2:
                october_middle_sum += df["distance"][i]
            elif df["discipline"][i] ==3:
                october_sprint_sum += df["distance"][i]
        elif df["date_month"][i] == 11:
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
    marker=dict(
        color='rgb(0, 143, 149)'
    ),
    opacity=0.9
    )
    trace2 = go.Bar(
    x= months,
    y=[march_middle_sum, april_middle_sum, may_middle_sum, june_middle_sum,
       september_middle_sum, october_middle_sum, november_middle_sum],
    name='middle',
    marker=dict(
        color='rgb(226, 78, 66)'
    ),
    opacity=0.9
    )
    trace3 = go.Bar(
    x= months,
    y=[march_sprint_sum, april_sprint_sum, may_sprint_sum, june_sprint_sum,
       september_sprint_sum, october_sprint_sum, november_sprint_sum],
    name='sprint',
    marker=dict(
        color='rgb(233, 176, 0)'
    ),
    opacity=0.9
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(
    barmode='stack',
    yaxis=dict(
        title='kilometry'
    ),
    font=dict(
        family='sans-serif',
        size=14
    ),
    margin=go.Margin(
        l=60,
        t=40,
        b=50,
        pad=4
    )
    )

    fig = go.Figure(data=data, layout=layout)
    fig_plot = plotly.offline.plot(fig, output_type='div')
    return fig_plot

def km_by_discipline(data_frame):
    df=data_frame
    rows = len(df.index)

    sum_km_long = 0
    sum_km_middle = 0
    sum_km_sprint = 0

    statistics=[]

    for i in range (rows):
        if df['time_min'][i] == 0:
            continue
        if df['discipline'][i] == 1:
            sum_km_long += df['distance'][i]
        elif df['discipline'][i] == 2:
            sum_km_middle += df['distance'][i]
        elif df['discipline'][i] == 3:
            sum_km_sprint += df['distance'][i]

    sum_km_long = str(round(sum_km_long, 2))
    sum_km_middle = str(round(sum_km_middle, 2))
    sum_km_sprint = str(round(sum_km_sprint, 2))

    statistics.extend((sum_km_long, sum_km_middle, sum_km_sprint))
    return statistics


def bar_graph_stacked_controls(data_frame):
    df = data_frame
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
        if df['time_min'][i] == 0:
            continue
        if df["date_month"][i] == 3:
            if df["discipline"][i] == 1:
                march_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                march_middle_sum += df["controls"][i]
            elif df["discipline"][i] == 3:
                march_sprint_sum += df["controls"][i]
        elif df["date_month"][i] == 4:
            if df["discipline"][i] == 1:
                april_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                april_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                april_sprint_sum += df["controls"][i]
        elif df["date_month"][i] == 5:
            if df["discipline"][i] == 1:
                may_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                may_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                may_sprint_sum += df["controls"][i]
        elif df["date_month"][i] == 6:
            if df["discipline"][i] == 1:
                june_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                june_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                june_sprint_sum += df["controls"][i]
        elif df["date_month"][i] == 9:
            if df["discipline"][i] == 1:
                september_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                september_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                september_sprint_sum += df["controls"][i]
        elif df["date_month"][i] == 10:
            if df["discipline"][i] == 1:
                october_long_sum += df["controls"][i]
            elif df["discipline"][i] == 2:
                october_middle_sum += df["controls"][i]
            elif df["discipline"][i] ==3:
                october_sprint_sum += df["controls"][i]
        elif df["date_month"][i] == 11:
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
    marker=dict(
        color='rgb(0, 143, 149)'
    ),
    opacity=0.9
    )
    trace2 = go.Bar(
    x= months,
    y=[march_middle_sum, april_middle_sum, may_middle_sum, june_middle_sum,
       september_middle_sum, october_middle_sum, november_middle_sum],
    name='middle',
    marker = dict(
        color='rgb(226, 78, 66)'
    ),
    opacity=0.9
    )
    trace3 = go.Bar(
    x= months,
    y=[march_sprint_sum, april_sprint_sum, may_sprint_sum, june_sprint_sum,
       september_sprint_sum, october_sprint_sum, november_sprint_sum],
    name='sprint',
    marker=dict(
        color='rgb(233, 176, 0)'
    ),
    opacity=0.9
    )
    data = [trace1, trace2, trace3]
    layout = go.Layout(
    barmode='stack',
    yaxis=dict(
        title='kontroly'
    ),
    font=dict(
        family='sans-serif',
        size=14
    ),
    margin=go.Margin(
        l=60,
        t=40,
        b=50,
        pad=4
    )
    )

    fig = go.Figure(data=data, layout=layout)
    fig_plot = plotly.offline.plot(fig, output_type='div')
    return fig_plot

def controls_by_discipline(data_frame):
    df=data_frame
    rows = len(df.index)

    sum_controls_long = 0
    sum_controls_middle = 0
    sum_controls_sprint = 0

    statistics=[]

    for i in range (rows):
        if df['time_min'][i] == 0:
            continue
        if df['discipline'][i] == 1:
            sum_controls_long += df['controls'][i]
        elif df['discipline'][i] == 2:
            sum_controls_middle += df['controls'][i]
        elif df['discipline'][i] == 3:
            sum_controls_sprint += df['controls'][i]

    sum_controls_long = str(round(sum_controls_long, 2))
    sum_controls_middle = str(round(sum_controls_middle, 2))
    sum_controls_sprint = str(round(sum_controls_sprint, 2))

    statistics.extend((sum_controls_long, sum_controls_middle, sum_controls_sprint))
    return statistics





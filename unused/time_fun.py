
import pandas as pd
import sqlite3
from convert_data import graphs_data

from datetime import datetime
from datetime import timedelta

def text_data(dataFrame):
    df = dataFrame
    rows = len(df.index)

    sum_time_hr = str(round(df['time_min'].sum()/60,2))
    sum_km = str(round(df['distance'].sum(),2))
    sum_controls = str(df['controls'].sum())

    print(sum_time_hr)
    print(sum_km)
    print(sum_controls)

    # lists for paces in specific disciplines
    pace_long = []
    pace_middle = []
    pace_sprint = []
    for i in range (rows):
        if df['time_min'][i] == 0:
            continue
        pace = df['time_min'][i]/df['distance'][i]
        if df['discipline'][i] == 1:
            pace_long.append(pace)
        elif df['discipline'][i] == 2:
            pace_middle.append(pace)
        elif df['discipline'][i] == 3:
            pace_sprint.append(pace)

    pace_long_mean = str(round(sum(pace_long)/len(pace_long),2))
    pace_long_min = str(round(min(pace_long),2))
    pace_long_max = str(round(max(pace_long),2))

    pace_middle_mean = str(round(sum(pace_middle)/len(pace_middle),2))
    pace_middle_min = str(round(min(pace_middle),2))
    pace_middle_max = str(round(max(pace_middle),2))

    pace_sprint_mean = str(round(sum(pace_sprint)/len(pace_sprint),2))
    pace_sprint_min = str(round(min(pace_sprint),2))
    pace_sprint_max = str(round(max(pace_sprint),2))


    # list to put the values in
    statistics = []
    statistics.extend((sum_time_hr, sum_km, sum_controls,
                       pace_long_mean, pace_long_min, pace_long_max,
                       pace_middle_mean, pace_middle_min, pace_middle_max,
                       pace_sprint_mean, pace_sprint_min, pace_sprint_max))
    return statistics

def km_by_discipline(data_frame):
    df=data_frame
    rows = len(df.index)

    sum_km_long = 0
    sum_km_middle = 0
    sum_km_sprint = 0

    statistics=[]

    for i in range (rows):
        if df["discipline"][i] == 1:
            sum_km_long += df["distance"][i]
        elif df['discipline'][i] == 2:
            sum_km_middle += df['distance'][i]
        elif df['discipline'][i] == 3:
            sum_km_sprint += df['distance'][i]

    sum_km_long = str(round(sum_km_long, 2))
    sum_km_middle = str(round(sum_km_middle, 2))
    sum_km_sprint = str(round(sum_km_sprint, 2))

    statistics.extend((sum_km_long, sum_km_middle, sum_km_sprint))
    return statistics





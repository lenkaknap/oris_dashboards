import sqlite3
import pandas as pd
import numpy as np
from pandas import to_datetime

# saves rows as tuple into a list, values in a specific "column"/position can be accessed through [i]
def all_info(person_id):
    conn = sqlite3.connect('orisdb.db')
    cur = conn.cursor()
    cur.execute('''select * from results
                left join races on results.eventId = races.id
                left join classes on results.classId=classes.id
                left join registered on results.userId=registered.id
                left join clubs on registered.clubId = clubs.id
                where userId = ?''', [person_id])
    rows = []
    for r in cur.fetchall():
        rows.append(r)
    conn.close()
    return rows

# saves rows as sqlite3.Row into a list, values in a specific column/position can be accessed through ["column_name"]
def all_info_row(person_id):
    conn = sqlite3.connect('orisdb.db')
    with conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('''select * from results
                left join races on results.eventId = races.id
                left join classes on results.classId=classes.id
                left join registered on results.userId=registered.id
                left join clubs on registered.clubId = clubs.id
                where userId = {}'''.format(person_id))
        rows = cur.fetchall()
    conn.close()
    return rows

# uses pandas function and changes the sql query response into a dataframe
def all_info_pandas_df(person_id):
    conn = sqlite3.connect("orisdb.db")
    if not isinstance(person_id, int):
        raise Exception('person id is not int, I am not putting this into DB')

    dataFrame = pd.read_sql_query('''select * from results
                                left join races on results.eventId = races.id
                                left join classes on results.classId=classes.id
                                left join registered on results.userId=registered.id
                                left join clubs on registered.clubId = clubs.id
                                where userId = %s''' %person_id, conn)
    conn.close()
    return dataFrame

# selecting only relevant columns for the map with markers
def map_data(person_id):
    conn = sqlite3.connect("orisdb.db")
    dataFrame = pd.read_sql_query('''select name, discipline, results.classTxt, latitude, longitude, date from results
                                    left join races on results.eventId = races.id
                                    where userId = %s''' % person_id, conn)
    conn.close()
    return dataFrame

def kilometers_data(person_id):
    from pandas import to_datetime
    conn = sqlite3.connect("orisdb.db")
    dataFrame = pd.read_sql_query('''select "date", discipline, distance, controls  from results
                                    left join races on results.eventId = races.id
                                    left join classes on results.classId=classes.id
                                    where userId = %s''' % person_id, conn)
    conn.close()
    # changing date to month only, dont care about the rest for now
    dataFrame["date"] = to_datetime(dataFrame["date"]).dt.month
    return dataFrame

def time_data(person_id):
    conn = sqlite3.connect("D:\oris_files\oris\orisdb.db")
    dataFrame = pd.read_sql_query('''select "date", discipline, distance, controls, time from results
                                    left join races on results.eventId = races.id
                                    left join classes on results.classId=classes.id
                                    where userId = %s''' % person_id, conn)
    conn.close()
    # changing date to month only, dont care about the rest for now

    dataFrame['date'] = to_datetime(dataFrame['date']).dt.month
    dataFrame['time_min']=""
    rows = len(dataFrame.index)
    for row in range (rows):
        minutes = 0.00
        seconds = 0.00
        if dataFrame['time'][row] == 'DISK':
            dataFrame['time_min'][row] = 0
        else:
            minutes, seconds = dataFrame['time'][row].split(":", 1)
            dataFrame['time_min'][row] = float(minutes) + float(seconds) / 60
    return dataFrame

def find_users (name):
    conn = sqlite3.connect("orisdb.db")
    cur = conn.cursor()
    cur.execute('''select registered.id, firstName, lastName, regNo, clubTxt from registered
                    LEFT JOIN clubs on registered.clubId = clubs.id
                    where lastName LIKE ?''', [name+'%'])
    rows = []
    for r in cur.fetchall():
        rows.append(r)
    conn.close()
    return rows

def get_user_data (oris_id):
    conn = sqlite3.connect("orisdb.db")
    cur = conn.cursor()
    cur.execute('''select registered.id, firstName, lastName, regNo, clubTxt from registered
                    LEFT JOIN clubs on registered.clubId = clubs.id
                    where registered.id == ? ''', [oris_id])
    data = cur.fetchall()
    return data

# df = time_data(2812)
# print(df)

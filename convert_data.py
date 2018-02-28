import sqlite3
import pandas as pd
from pandas import to_datetime

import os
cur_dir = os.path.dirname(os.path.abspath(__file__))
db_location = cur_dir + '/orisdb.db'


def find_users (name):
    conn = sqlite3.connect(db_location)
    cur = conn.cursor()
    cur.execute('''SELECT registered.id, firstName, lastName, regNo, clubTxt FROM registered
                    LEFT JOIN clubs ON registered.clubId = clubs.id
                    WHERE lastName LIKE ?''', (name+'%',))
    rows = []
    for r in cur.fetchall():
        rows.append(r)
    conn.close()
    return rows


def get_user_data (oris_id):
    conn = sqlite3.connect(db_location)
    cur = conn.cursor()
    cur.execute('''SELECT registered.id, firstName, lastName, regNo, clubTxt FROM registered
                    LEFT JOIN clubs ON registered.clubId = clubs.id
                    WHERE registered.id == ? ''', [oris_id])
    data = cur.fetchall()
    conn.close()
    return data

# uses pandas function and changes the sql query response into a dataframe
def graphs_data(person_id):
    conn = sqlite3.connect(db_location)
    # if not isinstance(person_id, int):
    #     raise Exception('person id is not int, I am not putting this into DB')

    dataFrame = pd.read_sql_query('''SELECT level, discipline, name, results.classTxt, date, latitude, longitude, distance, climbing, controls, time  FROM results
                                LEFT JOIN races ON results.eventId = races.id
                                LEFT JOIN classes ON results.classId=classes.id
                                WHERE userId = %s''' %person_id, conn)
    conn.close()

    dataFrame['date_month'] = to_datetime(dataFrame['date']).dt.month
    dataFrame['time_min'] = ""
    rows = len(dataFrame.index)
    unwanted = ['DISK', 'VZDAL', 'DNS']

    for row in range(rows):
        if dataFrame['time'][row] in unwanted or dataFrame['time'][row] == None:
            dataFrame['time_min'][row] = 0
        else:
            minutes, seconds = dataFrame['time'][row].split(":", 1)
            dataFrame['time_min'][row] = float(minutes) + float(seconds) / 60
    return dataFrame
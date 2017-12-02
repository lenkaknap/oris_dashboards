import sqlite3
import pandas as pd

# below are three ways to get data from db, the third one - dataFrame - might be the best for use with pandas (and other libraries as well?)
# not sure as of now, in which format I'll need the data for specific analyses, will be adding specific methods later
# I had some trouble with adding the 'person_id' parameter to the SQL query, especially in the all_info_pandas_df
# the solution seems to work but PyCharm doesn't like the syntax, not sure why


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
    from pandas import to_datetime
    conn = sqlite3.connect("orisdb.db")
    dataFrame = pd.read_sql_query('''select "date", discipline, distance, controls, time, startTime, finishTime  from results
                                    left join races on results.eventId = races.id
                                    left join classes on results.classId=classes.id
                                    where userId = %s''' % person_id, conn)
    conn.close()
    # changing date to month only, dont care about the rest for now
    dataFrame["date"] = to_datetime(dataFrame["date"]).dt.month
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

# testovaci vystupy metod
# all_info = all_info(2812)
# print(all_info)
#
# all_info2 = all_info_row(2812)
# print(all_info2)
#
# all_info_df = all_info_pandas_df(2812)
# print(all_info_df)
#
# map_df = map_data(2812)
# print(map_df)

# time_df = time_data(2812)
# print(time_df)

# users = find_users('Knap')
# print(users)
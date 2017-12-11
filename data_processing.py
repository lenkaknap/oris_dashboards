import requests
import csv

def save_into_file(file_name, fieldnames, data):
    with open('{file_name}.csv'.format(file_name=file_name), 'w+', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for d in data:
            writer.writerow(d)

def load_from_csv(file_name, fieldnames):
    raw_data = []
    with open('{file_name}.csv'.format(file_name=file_name), 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file, fieldnames=fieldnames, delimiter=";")
        next(reader)  # skip header
        for row in reader:
            raw_data.append(row)
    return raw_data

# api request info for EVENTS/RACES
homepage = 'https://oris.orientacnisporty.cz/API/'
payload = {
    'format': 'json',
    'method': 'getEventList',
    'sport': '1',  # foot orienteering
    'level': '1,3,4,8,11',  # selecting only czechChamps, ALevel, BLevel, Local+LocalChamps
    'datefrom': '2017-01-01'}
r = requests.get(homepage, params=payload)
r_json = r.json()


# EVENTS/RACES
events = []
wanted_discipline = ['1', '2', '3'] # I only want sprint, middle and long races (not other disciplines)
for event in r_json["Data"].values():
    # I only want sprint, middle and long races (not other disciplines) and I don't want cancelled races
    if event["Discipline"]["ID"] not in wanted_discipline or event["Cancelled"] == '1':
        continue
    ev = dict(id=event["ID"], name=event["Name"], date=event["Date"],
              discipline=event["Discipline"]["ID"], disciplineTxt=event["Discipline"]["ShortName"],
              disciplineCZ=event["Discipline"]["NameCZ"], disciplineEN=event["Discipline"]["NameEN"],
              level=event["Level"]["ID"], levelCZ=event["Level"]["NameCZ"], levelEN=event["Level"]["NameEN"],
              latitude=event["GPSLat"], longitude=event["GPSLon"], place=event["Place"], ranking=event["Ranking"])
    events.append(ev)
eventFieldnames = ['id', 'name', 'date', 'discipline', 'disciplineTxt', 'disciplineCZ', 'disciplineEN',
                    'level', 'levelCZ', 'levelEN', 'latitude', 'longitude', 'place', 'ranking']
save_into_file(file_name='races', fieldnames=eventFieldnames, data=events)

# loading data to do RESULTS and CLASSES
myData = load_from_csv('races', eventFieldnames)

# RESULTS
results = []
for d in myData:
    payload.update({'method': 'getEventResults', 'eventid': d['id']})
    r = requests.get(homepage, params=payload)
    r_json = r.json()
    for result in r_json["Data"].values():
        if result["UserID"] == None:
            continue
        res = dict(id=result["ID"], eventId=d["id"], classId=result["ClassID"],
                   classTxt=result["ClassDesc"], userId=result["UserID"],
                   name=result["Name"], regNo=result["RegNo"], sort=result["Sort"],
                   time=result["Time"], loss=result["Loss"],
                   startTime=result["StartTime"], finishTime=result["FinishTime"])
        results.append(res)
resultsFieldnames = ['id', 'eventId', 'classId', 'classTxt', 'userId',
                     'name', 'regNo', 'sort', 'time', 'loss', 'startTime', 'finishTime']
save_into_file('results', resultsFieldnames, results)

# CATEGORIES/CLASSES using my data as well
classes = []
for d in myData:
    payload.update({'method': 'getEvent', 'id': d['id']})
    r = requests.get(homepage, params=payload)
    r_json = r.json()
    for cla in r_json["Data"]["Classes"].values():
        cla = dict(id=cla["ID"], eventId=d["id"], classTxt=cla["Name"], distance=cla["Distance"],
                   climbing=cla["Climbing"], controls=cla["Controls"], )
        classes.append(cla)
classesFieldnames = ['id', 'eventId', 'classTxt', 'distance', 'climbing', 'controls']
save_into_file(file_name='classes', fieldnames=classesFieldnames, data=classes)

# USERS - registered runners
users = []
payload.update({'method': 'getRegistration', 'sport': '1', 'year': '2017'})
r = requests.get(homepage, params=payload)
r_json = r.json()
for user in r_json["Data"].values():
    us = dict(id=user["UserID"], regNo=user["RegNo"],
              name=user["FirstName"], surname=user["LastName"],
              license=user["Lic"], clubId=user["ClubID"])
    users.append(us)
usersFieldnames = ['id', 'regNo', 'name', 'surname', 'license', 'clubId']
save_into_file('registered17', usersFieldnames, users)

# CLUBS
clubs = []
payload.update({'method': 'getCSOSClubList'})
r = requests.get(homepage, params=payload)
r_json = r.json()
for club in r_json["Data"].values():
    cl = dict(id=club["ID"], clubTxt=club["Name"],
              clubAbbr=club["Abbr"])
    clubs.append(cl)
clubsFieldnames = ['id', 'clubTxt', 'clubAbbr']
save_into_file('clubs', clubsFieldnames, clubs)

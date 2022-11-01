from apple_calendar_integration import *
from datetime import datetime, timedelta

def write(username, password, edate, time, occurence, code, room, lecturer):
    api = ICloudCalendarAPI(username, password)
    Duration = time.split(" - ")
    Starttime = datetime.strptime(Duration[0], '%H:%M').time()
    Endtime = datetime.strptime(Duration[1], '%H:%M').time()
    start_date = date(weekday(edate))
    startdatetime = datetime.combine(start_date, Starttime)
    enddatetime = datetime.combine(start_date, Endtime)
    
    alarm = {
        "before": False,
        "hours": 1,
        "minutes": 15,
        "days": 1
    }

    note = "Room: " + room + "\nLecturer: " + lecturer + "\nOccurence: " + occurence

    etag, ctag, guid = api.create_event(code, startdatetime, enddatetime, alarm=alarm, note=note)

def weekday(weekday):
    if weekday == "Mon":
        return 0
    elif weekday == "Tue":
        return 1
    elif weekday == "Wed":
        return 2
    elif weekday == "Thu":
        return 3
    elif weekday == "Fri":
        return 4
    elif weekday == "Sat":
        return 5
    elif weekday == "Sun":
        return 6

def date(weekday):
    now = datetime.now()
    day = now - (timedelta(days = now.weekday()) - (timedelta(days = weekday)))
    date = day.date()
    return date




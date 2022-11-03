from apple_calendar_integration import *
from icalendar import Calendar, Event, vText, Alarm
from datetime import datetime, timedelta

def write(username, password, edate, time, occurence, code, room, lecturer):
    Duration = time.split(" - ")
    Starttime = datetime.strptime(Duration[0], '%H:%M').time()
    Endtime = datetime.strptime(Duration[1], '%H:%M').time()
    start_date = date(weekday(edate))
    startdatetime = datetime.combine(start_date, Starttime)
    enddatetime = datetime.combine(start_date, Endtime)

    Class = Event()
    Class.add('summary', code)
    Class.add('description', "Lecturer: " + lecturer + "\nOccurence: " + occurence)
    Class.add('dtstart', startdatetime)
    Class.add('dtend', enddatetime)
    Class['location'] = vText(room)

    alarm1 = Alarm()
    alarm1.add('action', 'DISPLAY')
    alert_time1 = timedelta(minutes=-int(15))
    alarm1.add('trigger', alert_time1)
    Class.add_component(alarm1)

    alarm2 = Alarm()
    alarm2.add('action', 'DISPLAY')
    alert_time2 = timedelta(hours=-int(1))
    alarm2.add('trigger', alert_time2)
    Class.add_component(alarm2)

    return Class

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
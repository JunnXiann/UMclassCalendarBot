from apple_calendar_integration import *
from datetime import datetime, timedelta
import re

def write(username, password, time, occurence, code, semester, type, campus, room, lecturer):
    api = ICloudCalendarAPI(username, password)
    alarm = {
        "before": False,
        "hours": 1,
        "minutes": 15,
        "days": 1
    }
    Duration = time.split(" - ")
    Starttime = datetime.strptime(Duration[0], '%H:%M')
    Endtime = datetime.strptime(Duration[1], '%H:%M')
    note = "Room: " + room + "\nLecturer: " + lecturer
    new_etag = api.edit_event(etag, ctag, guid, alarm=alarm, note=note, start_date)




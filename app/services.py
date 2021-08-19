from typing import Dict, List
import json
import datetime as dt


def get_all_events() -> Dict:
    with open('data.json', 'r') as data_file:
        events = json.load(data_file)
        return events


def month_events(month: str) -> Dict:
    month = month.lower()
    events = get_all_events()
    try:
        month_events = events[month]
        return month_events
    except:
        return "INVALID MONTH !!"


def day_events(month: str, day: int) -> List:
    month = month.lower()
    events = get_all_events()
    try:
        day_evnts = events[month][str(day)]
        return day_evnts
    except:
        return "INVALID MONTH !!"


def events_today():
    today = dt.date.today()
    month = today.strftime("%B").lower()
    return day_events(month, today.day)

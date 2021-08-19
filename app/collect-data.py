import datetime as dt
from typing import Iterator, Dict
import scrapper
import json


def date_range(startdate: dt.date, enddate: dt.date) -> Iterator:
    for i in range(int((enddate-startdate).days)):
        yield startdate + dt.timedelta(i)


def create_events_dict() -> Dict:
    events = dict()
    startdate = dt.date(2021, 1, 1)
    enddate = dt.date(2022, 1, 1)
    for date in date_range(startdate, enddate):
        month = date.strftime("%B").lower()
        if month not in events:
            events[month] = dict()
        events[month][date.day] = scrapper.get_events(month, date.day)
    return(events)


if __name__ == "__main__":
    events = create_events_dict()
    data_file = open("data.json", "w")
    json.dump(events, data_file, ensure_ascii=False)
    data_file.close()

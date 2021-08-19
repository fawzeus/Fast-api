import bs4
import requests
from typing import List


def generate_url(month: str, day: int) -> str:
    return f"https://www.onthisday.com/day/{month}/{day}"


def get_page(url: str) -> str:
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    return soup


def get_events(month: str, day: int) -> List[str]:
    url = generate_url(month, day)
    page = get_page(url)
    events = page.find_all(class_="event")
    events = [event.text for event in events]
    return (events)


get_events("april", 3)

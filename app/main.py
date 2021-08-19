from fastapi import FastAPI
import services
app = FastAPI()


@app.get('/')
async def index():
    return {"data": "Welcome !!"}


@app.get("/events")
async def get_events():
    return services.get_all_events()


@app.get('/events/today')
async def event_today():
    return services.events_today()


@app.get("/events/{month}")
async def get_month_events(month: str):
    return services.month_events(month)


@app.get("/events/{month}/{day}")
async def get_day_events(month: str, day: int):
    return services.day_events(month, day)

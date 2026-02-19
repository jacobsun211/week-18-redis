from fastapi import FastAPI
from dal import alerts_by_border_and_priority



app = FastAPI()

@app.get("/analytics/alerts-by-border-and-priority")
def get_alerts_by_border_and_priority():
    answer = alerts_by_border_and_priority()
    response = []
    for row in answer:
        response.append(row)
    return response
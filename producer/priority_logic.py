from redis_connection import urgent_queue,normal_queue
from models import Alert
import json



def send_to_redis(alert):
    priority = alert["priority"]
    
    alert = json.dumps(alert)
    if priority == "URGENT":
        urgent_queue.set(priority,alert) 

    elif priority == "NORMAL":
        normal_queue.set(priority,alert)


def priority_check(alert):
    # i wanted to do all the condition in list but there was no time
    if alert["weapons_count"] > 0:
        alert["priority"] = "URGENT"

    elif alert["distance_from_fence_m"] <= 50:
        alert["priority"] = "URGENT"

    elif alert["people_count"] >= 8:
        alert["priority"] = "URGENT"

    elif alert["vehicle_type"] == "truck":
        alert["priority"] = "URGENT"
    
    elif (alert["distance_from_fence_m"] <= 150 and alert["people_count"] >= 4):
         alert["priority"] = "URGENT"

    # combined conditions
    elif (alert["distance_from_fence_m"] <= 150 and alert["people_count"] >= 4):
        alert["priority"] = "URGENT"

    elif (alert["vehicle_type"] == "jeep" and alert["people_count"] >= 3):
        alert["priority"] = "URGENT"
    
    else:
         alert["priority"] = "NORMAL"
    
    return alert

    
       



def producer():
    with open("border_alerts.json", "r", encoding="utf-8") as f:
                alerts = json.load(f)
    for alert in alerts:
        # alert = Alert(alert) # validation
        alert = priority_check(alert)
        send_to_redis(alert)
         

    


producer()



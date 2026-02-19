from redis_connection import urgent_queue, normal_queue
from mongo_connection import collection
import datetime
import json


def insert_to_mongo(alert):
    collection.insert_one(alert)
    urgent_queue.delete(alert["priority"])

def consumer():
    while True:
        alert = urgent_queue.get("URGENT")
        if not alert:
            alert = normal_queue.get("NORMAL")
        if not alert: continue

        alert = json.loads(alert) # from str to dict
        alert["insertion_time"] = datetime.datetime.now()
        insert_to_mongo(alert)

if __name__ == "__main__":
    consumer()
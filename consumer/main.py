from redis_connection import urgent_queue, normal_queue
from mongo_connection import collection
import datetime
import json


def insert_to_mongo(alert):
    collection.insert_one(alert)
    return

def consumer():
    while True:
        alert = urgent_queue.lpop("URGENT")
        if not alert:
            alert = normal_queue.lpop("NORMAL")
        if not alert: continue

        alert = json.loads(alert) # from str to dict
        alert["insertion_time"] = datetime.datetime.now()
        insert_to_mongo(alert)

if __name__ == "__main__":
    consumer()



from redis_connection import urgent_queue, normal_queue, querys
from mongo_connection import collection
import json

def send_to_redis(query_num, answer):
    answer = json.dumps(answer)
    urgent_queue.set(query_num,answer)


def alerts_by_border_and_priority():
    query_num = "1"
    # checking if the answer in redis
    answer = querys.get(query_num)
    if answer is not None:
        answer = json.loads(answer)
        return answer
    answer = collection.find({"priority":"URGENT"},
                        {"zone":1, "_id":0}
                        )
    send_to_redis(query_num, answer)
    return answer


def top_urgent_zones():
    query_num = "2"
    # checking if the answer in redis
    answer = querys.get(query_num)
    if answer is not None:
        answer = json.loads(answer)
        return answer
    query = [
    {'$group': {'zone':"$tags", "count": {"$sum":1}}}
]
    answer = collection.aggregate(query)
    send_to_redis(query_num, answer)
    return answer
    

def distance_distribution():
    query_num = "2"
    # checking if the answer in redis
    answer = querys.get(query_num)
    if answer is not None:
        answer = json.loads(answer)
        return answer
    query = {
        'distance_from_fence_m':{'$gte': 1, '$lte': 300}}
     # i had to stop here since there was no time, didnt finish the query
    answer = collection.aggregate(query)
    send_to_redis(query_num, answer)
    return answer
    
    
    

        
    


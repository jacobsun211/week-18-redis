import redis 


urgent_queue = redis.Redis(host='localhost', port=6379, decode_responses=True, db = 0)

normal_queue = redis.Redis(host='localhost', port=6379, decode_responses=True, db = 1)


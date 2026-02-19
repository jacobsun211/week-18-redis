import redis 


r = redis.Redis(host='localhost', port=6379, decode_responses=True, db = 0)

r1 = redis.Redis(host='localhost', port=6379, decode_responses=True, db = 1)


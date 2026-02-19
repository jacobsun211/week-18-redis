import redis 
# # Source - https://stackoverflow.com/a/8986285
# # Posted by Simon Klee, modified by community. See post 'Timeline' for change history
# # Retrieved 2026-02-19, License - CC BY-SA 3.0

# >>> pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# >>> r = redis.StrictRedis(connection_pool=pool)



r = redis.Redis(host='localhost', port=6379, decode_responses=True, db = 0)

r1 = redis.Redis(host='localhost', port=6379, decode_responses=True, db = 1)


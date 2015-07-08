__author__ = 'adminweke'
import redis

r = redis.StrictRedis(host='113.142.35.45', port='6379', db=0, password='passwordIsCocopie2014')
# r = redis.StrictRedis(host='113.142.35.45', port='6379', db=0)
# r.set('python_str', 'Hello Python Redis')
print r.get('python_str')

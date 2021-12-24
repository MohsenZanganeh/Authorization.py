import config
from redis import Redis

class rdb():
    def __init__(self):
        self.client = Redis(
            host = config.REDIS['host'],
            port = config.REDIS['port'],
            db   = config.REDIS['db'])       

    def hset(self,path, key, value):
        return self.client.hset(path,key,value)
    
    def hdel(self,path, key):
        return self.client.hdel(path,key)

    def hget(self,path, key):
        return self.client.hget(path,key)

    def hkeys(self,path):
        return self.client.hkeys(path)

    def get(self,path):
        return self.client.get()


    def flushdb(self):
        return self.client.flushdb()
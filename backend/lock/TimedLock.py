import redis


class TimedLock:
    DATABASE = 0

    def __init__(self, redis_host, redis_port) -> None:
        self.__redis_host = redis_host
        self.__redis_port = redis_port
        self.__client = None

    def set_lock(self, key, seconds):
        return self.__get_client().set(key, "1", ex = seconds)

    def has_lock(self, key):
        if None == self.__get_client().get(key):
            return False

        return True

    def __get_client(self):
        if None != self.__client:
            return self.__client

        self.client = redis.StrictRedis(host = self.__redis_host, port = self.__redis_port, db = self.DATABASE)

        return self.client

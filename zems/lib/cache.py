import os
import pickle
from time import time


class Cache:
    def __init__(self):
        pass

    @staticmethod
    def write(name, data):
        try:
            with open("/tmp/zems-%s" % name, "w") as tmpfile:
                pickle.dump(data, tmpfile)
        except OSError:
            pass
        except pickle.PickleError:
            pass

    @staticmethod
    def read(name, ttl=59):
        if Cache.is_expired(name, ttl):
            return None

        try:
            with open("/tmp/zems-%s" % name, "r") as tmpfile:
                return pickle.load(tmpfile)
        except OSError:
            return None
        except pickle.PickleError:
            return None

    @staticmethod
    def is_expired(name, ttl):
        try:
            if os.path.getmtime("/tmp/zems-%s" % name) <= (time() - ttl):
                return True
        except OSError:
            return True

        return False
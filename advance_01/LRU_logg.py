import sys
import logging
import logging.config
from collections import deque


log_conf = {
    "version": 1,
    "formatters": {
        "simple": {"format": "%(asctime)s\t%(levelname)s\t%(message)s"},
        "processed": {
            "format": "[%(levelname)s - %(module)s - %(funcName)s] %(message)s",
        },
    },
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "filename": "cache.log",
            "formatter": "simple",
        },
        "stream_handler": {
            "level": "DEBUG",
            "formatter": "processed",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "file": {"level": "DEBUG", "handlers": ["file_handler"]},
        "total": {"level": "DEBUG", "handlers": ["file_handler", "stream_handler"]},
    },
}


logging.config.dictConfig(log_conf)
param = sys.argv[1] if len(sys.argv) > 1 else None
if param == "-s":
    logger = logging.getLogger("total")
else:
    logger = logging.getLogger("file")


class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.queue = deque([])
        if capacity < 0:
            logger.critical("Capacity must be > 0. Capacity given: %d", capacity)
            return
        self.capacity = capacity
        logger.debug("Item created with capacity: %d", capacity)

    def update_queue(self, key: str):
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

    def get_value(self, key: str):
        if key in self.dict.keys():
            self.update_queue(key)
            return self.dict[key]
        logger.info("There is no such: %s", key)
        return None

    def set_value(self, key: str, value: str):
        if key not in self.dict.keys() and len(self.dict) >= self.capacity:
            k = self.queue.popleft()
            del self.dict[k]
            logger.info("Key - %s is deleted", key)
        self.update_queue(key)
        self.dict[key] = value
        logger.debug("Added key: %s with value: %s", key, value)

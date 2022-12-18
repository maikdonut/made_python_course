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
        "total": {"level": "INFO", "handlers": ["file_handler", "stream_handler"]},
    },
}


logging.config.dictConfig(log_conf)
file_logger = logging.getLogger("file")
total_logger = logging.getLogger("total")


class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.queue = deque([])
        if capacity < 0:
            total_logger.critical("Capacity must be > 0. Capacity given: %d", capacity)
            return
        self.capacity = capacity
        file_logger.debug("Item created with capacity: %d", capacity)

    def update_queue(self, key: str):
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

    def get_value(self, key: str):
        if key in self.dict.keys():
            self.update_queue(key)
            return self.dict[key]
        total_logger.info("There is no such: %s", key)
        return None

    def set_value(self, key: str, value: str):
        if key not in self.dict.keys() and len(self.dict) >= self.capacity:
            k = self.queue.popleft()
            del self.dict[k]
            total_logger.info("Key - %s is deleted", key)
        self.update_queue(key)
        self.dict[key] = value
        file_logger.debug("Added key: %s with value: %s", key, value)

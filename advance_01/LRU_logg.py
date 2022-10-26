import logging
from collections import deque

logger = logging.getLogger("cache")
logging.basicConfig(
    filename="cache.log",
    level=logging.INFO,
    format="%(asctime)s\t%(levelname)s\t%(message)s",
)


class LRUCache:
    def __init__(self, capacity: int):
        self.dict = {}
        self.queue = deque([])
        if capacity < 0:
            logging.critical("Capacity must be > 0. Capacity given: %d", capacity)
            return
        self.capacity = capacity
        logging.info("Item created with capacity: %d", capacity)

    def update_queue(self, key: str):
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

    def get_value(self, key: str):
        if key in self.dict.keys():
            self.update_queue(key)
            return self.dict[key]
        logging.info("There is no such: %s", key)
        return None

    def set_value(self, key: str, value: str):
        if key not in self.dict.keys() and len(self.dict) >= self.capacity:
            k = self.queue.popleft()
            del self.dict[k]
            logging.info("Key - %s is deleted", key)
        self.update_queue(key)
        self.dict[key] = value
        logging.info("Added key: %s with value: %s", key, value)

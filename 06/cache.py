"""Implement list-like container with fast appends and pops on either end"""
from collections import deque


class LRUCache:
    """
    LRU cache using dict and deque
    """
    def __init__(self, capacity: int):
        self.dict = {}
        self.queue = deque([])
        self.capacity = capacity
        assert capacity > 0, "Capacity must be > 0"

    def update_queue(self, key: str):
        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

    def get_value(self, key: str):
        if key in self.dict.keys():
            self.update_queue(key)
            return self.dict[key]
        return None

    def set_value(self, key: str, value: str):
        if key not in self.dict.keys() and len(self.dict) >= self.capacity:
            k = self.queue.popleft()
            del self.dict[k]
        self.update_queue(key)
        self.dict[key] = value

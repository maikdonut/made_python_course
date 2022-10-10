import unittest
from collections import deque
from cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def test_set_value(self):
        self.cache = LRUCache(2)
        self.cache.set_value("k2", "val2")
        self.cache.set_value("k1", "val1")
        self.assertEqual(self.cache.queue, deque(["k2", "k1"]))
        self.assertEqual(self.cache.dict, {"k2": "val2", "k1": "val1"})
        self.cache.set_value("k3", "val3")
        self.assertEqual(self.cache.queue, deque(["k1", "k3"]))
        self.assertEqual(self.cache.dict, {"k3": "val3", "k1": "val1"})

    def test_get_value(self):
        self.cache = LRUCache(3)
        self.cache.set_value("k2", "val2")
        self.cache.set_value("k1", "val1")
        self.cache.set_value("k3", "val3")
        res = self.cache.get_value("k1")
        self.assertEqual(res, "val1")
        self.assertEqual(self.cache.queue, deque(["k2", "k3", "k1"]))
        res = self.cache.get_value("k4")
        self.assertEqual(res, None)


if __name__ == "__main__":
    unittest.main()

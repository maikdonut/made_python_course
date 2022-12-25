import time
from typing import Dict, Union

Number = Union[int, float, complex]


class BaseMetric:
    def __init__(self, name: str):
        self.__name__ = name

    def get_name(self):
        return self.name

    def get_value(self):
        pass

    def add(self, value: Number):
        pass

    def clear(self):
        pass


class MetricTimer(BaseMetric):
    def __init__(self, name: str):
        super().__init__(name)
        self.pr_time: Number
        self.start = 0
        self.pc_time = 0

    def add(self):
        self.pr_time = time.time() - self.start

    def get_value(self):
        return self.pr_time

    def clear(self):
        self.pr_time = 0
        self.start = 0

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_value, trace_b):
        self.pr_time = time.time() - self.start


class MetricAvg(BaseMetric):
    def __init__(self, name: str):
        super().__init__(name)
        self.value: Number
        self.count = 0
        self.value = 0

    def add(self, value: Number):
        self.count += 1
        self.value += value

    def get_value(self):
        return self.value / self.count

    def clear(self):
        self.count = 0
        self.value = 0


class MetricCount(BaseMetric):
    def __init__(self, name: str):
        super().__init__(name)
        self.count = 0

    def add(self):
        self.count += 1

    def get_value(self):
        return self.count

    def clear(self):
        self.count = 0


MetricClass = Union[MetricTimer, MetricAvg, MetricCount]


class Stats:
    timer_stat = {}
    avg_stat = {}
    count_stat = {}

    @classmethod
    def timer(cls, name: str):
        if not cls.timer_stat.get(name):
            cls.timer_stat[name] = MetricTimer(name)
        return cls.timer_stat[name]

    @classmethod
    def avg(cls, name: str):
        if not cls.avg_stat.get(name):
            cls.avg_stat[name] = MetricAvg(name)
        return cls.avg_stat[name]

    @classmethod
    def count(cls, name: str):
        if not cls.count_stat.get(name):
            cls.count_stat[name] = MetricCount(name)
        return cls.count_stat[name]

    @classmethod
    def collect(cls):
        cls_func = ["timer", "avg", "count"]
        stats = {}
        for i, metrics in enumerate([cls.timer_stat, cls.avg_stat, cls.count_stat]):
            for key in metrics.keys():
                if metrics[key].get_value() != 0:
                    stats[f"{key}.{cls_func[i]}"] = metrics[key].get_value()
            metrics.clear()
        return stats

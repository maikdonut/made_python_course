import unittest
import time
from metric_stats import Stats


class TestMyClass(unittest.TestCase):
    def test_metric_stats(self):
        def func():
            time.sleep(0.2)
            return 2

        with Stats.timer("func"):
            res = func()
        Stats.timer("func").add()
        Stats.count("func").add()
        Stats.avg("func").add(res)
        Stats.count("func").add()
        Stats.avg("func").add(res + 1)

        Stats.count("new_func").add()
        Stats.avg("new_func").add(0.5)
        Stats.count("new_func").add()
        Stats.avg("new_func").add(0.3)

        Stats.count("some_func").add()
        Stats.avg("some_func").add(0.222)
        Stats.count("no_used")

        metrics = Stats.collect()
        delt = 1

        self.assertAlmostEqual(metrics["func.timer"], 0.2, delt)
        self.assertAlmostEqual(metrics["func.avg"], 2.5, delt)
        self.assertEqual(metrics["func.count"], 2)

        self.assertAlmostEqual(metrics["new_func.avg"], 0.4, delt)
        self.assertEqual(metrics["new_func.count"], 2)

        self.assertAlmostEqual(metrics["some_func.avg"], 0.2, delt)
        self.assertEqual(metrics["some_func.count"], 1)

        metrics = Stats.collect()
        self.assertEqual(metrics, {})


if __name__ == "__main__":
    unittest.main()

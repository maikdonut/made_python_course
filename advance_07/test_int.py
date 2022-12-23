import unittest


class TestInt(unittest.TestCase):
    def test_int_different_base(self):
        self.assertEqual(int("0o12", 8), 10)
        self.assertEqual(int("0b110", 2), 6)
        self.assertEqual(int("0x1A", 16), 26)
        self.assertEqual(int("77", 10), 77)

    def test_int_from_float(self):
        self.assertEqual(int(9.999999), 9)
        self.assertEqual(int(100.0), 100)
        self.assertEqual(int(-22.5), -22)

    def test_int_exceptions(self):
        with self.assertRaises(TypeError):
            int(0b101, 2)
        with self.assertRaises(ValueError):
            int("python")
        with self.assertRaises(ValueError):
            (int("5.0"))


if __name__ == "__main__":
    unittest.main()

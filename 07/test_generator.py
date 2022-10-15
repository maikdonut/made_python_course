import unittest
from unittest.mock import patch, mock_open
from generator import processing


class Test(unittest.TestCase):

    data = "a b c\nx y z\n1 aa 3\nx y a"

    @patch("builtins.open", mock_open(read_data=data))
    def test_open_1(self):
        result = list(processing("a", "filename"))
        open.assert_called_once_with("filename", "r", encoding="utf-8")
        self.assertEqual(["a b c", "x y a"], result)

    data = "шла Саша по шоссе\nсаша и маша\n у саши болит зуб"

    @patch("builtins.open", mock_open(read_data=data))
    def test_open_2(self):
        result = list(processing("саша", "filename"))
        open.assert_called_once_with("filename", "r", encoding="utf-8")
        self.assertEqual(["шла Саша по шоссе", "саша и маша"], result)


if __name__ == "__main__":
    unittest.main()

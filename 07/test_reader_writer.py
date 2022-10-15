import unittest
from unittest.mock import patch, mock_open
from reader_writer import *


class BaseTestCases:
    class TestBaseReader(unittest.TestCase):
        def test_common(self):
            print("Calling TestBaseReader:test_common")

    class TestBaseWriter(unittest.TestCase):
        def test_common(self):
            print("Calling TestBaseWriter:test_common")


class TestTxtReader(BaseTestCases.TestBaseReader):
    data = "a,b,c\nx,y,z\n1,2,3"

    @patch("builtins.open", mock_open(read_data=data))
    def test_open_1(self):
        result = read_data("filename", TxtReader())
        open.assert_called_once_with("filename", "r")
        self.assertEqual(["a,b,c", "x,y,z", "1,2,3"], result)

    data = ["alpha", "beta", "gamma"]

    @patch("builtins.open", mock_open(read_data="\n".join(data)))
    def test_open_2(self):
        result = read_data("filename", TxtReader())
        open.assert_called_once_with("filename", "r")
        self.assertEqual(["alpha", "beta", "gamma"], result)


class TestJsonReader(BaseTestCases.TestBaseReader):
    data = {"name": "Alex", "age": 56, "id": 981286, "field of study": "NLP"}
    json_data = json.dumps(data)

    @patch("builtins.open", mock_open(read_data=json_data))
    def test_open(self):
        result = read_data("filename", JsonReader())
        open.assert_called_once_with("filename", "r")
        self.assertEqual(
            {"name": "Alex", "age": 56, "id": 981286, "field of study": "NLP"}, result
        )


class TestCsvReader(BaseTestCases.TestBaseReader):
    data = ["Carl Jacobi", "Leonard Euler", "Andrey Kolmogorov"]
    json_data = json.dumps(data)

    @patch("builtins.open", mock_open(read_data=json_data))
    def test_open(self):
        result = read_data("filename", CsvReader())
        open.assert_called_once_with("filename", "r")
        self.assertEqual(
            [['["Carl Jacobi"', ' "Leonard Euler"', ' "Andrey Kolmogorov"]']], result
        )


class TestTxtWriter(BaseTestCases.TestBaseWriter):
    data = "Samsung\nApple\nHuawei"
    open_mock = mock_open()
    with patch("reader_writer.open", open_mock, create=True):
        dump_data(data, "output.txt", TxtWriter())
    open_mock.assert_called_with("output.txt", "w")
    open_mock.return_value.write.assert_called_once_with("Samsung\nApple\nHuawei")


class TestJsonWriter(BaseTestCases.TestBaseWriter):
    data = {"name": "Peter", "number": 89991234567}
    open_mock = mock_open()
    with patch("reader_writer.open", open_mock, create=True):
        dump_data(data, "output.json", JsonWriter())
    open_mock.assert_called_with("output.json", "w")
    open_mock.return_value.write.assert_called_once_with(
        '{"name": "Peter", "number": 89991234567}'
    )


class TestCsvWriter(BaseTestCases.TestBaseWriter):
    data = ["Lionel Messi"]
    open_mock = mock_open()
    with patch("reader_writer.open", open_mock, create=True):
        dump_data(data, "output.csv", CsvWriter())
    open_mock.assert_called_with("output.csv", "w")
    open_mock.return_value.write.assert_called_once_with("L,i,o,n,e,l, ,M,e,s,s,i\r\n")


if __name__ == "__main__":
    unittest.main()

import unittest
from async_url import fetch_url
from unittest.mock import AsyncMock


class TestAsyncURLs(unittest.IsolatedAsyncioTestCase):
    async def test_fetch_url(self):
        my_mock = AsyncMock()
        my_mock.return_value = "Abcd Efgh"
        r = my_mock()
        awaited_result = await r
        res = len(awaited_result)
        self.assertEqual(res, len(await my_mock()))

    async def test_fetch_url_mock_generator(self):
        expected_values = ["12345", "some string", "7*7=49"]
        my_mock_generator = AsyncMock()
        my_mock_generator.__aiter__.return_value = expected_values

        actual_values = []
        async for value in my_mock_generator:
            actual_values.append(len(value))
        expected_values_len = [len(i) for i in expected_values]
        self.assertListEqual(expected_values_len, actual_values)


if __name__ == "__main__":
    unittest.main()

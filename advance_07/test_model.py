import unittest
from unittest.mock import patch, call
from model import SomeModel, custom_prediction, predict_message_mood


class TestModel(unittest.TestCase):
    def test_custom_prediction(self):
        delt = 2
        self.assertAlmostEqual(custom_prediction("Abc Def"), 0, delt)
        self.assertAlmostEqual(custom_prediction("abc 123 \n"), 0.333, delt)
        self.assertAlmostEqual(custom_prediction("248610121416"), 1, delt)

    def test_predict_message_mood_empty_message(self):
        res = predict_message_mood("", SomeModel)
        self.assertEqual(res, "Empty message")

    def test_predict_message_mood(self):
        with patch("model.SomeModel.predict") as m_model_predict:
            m_model_predict.return_value = 0.5

            res = predict_message_mood("abc123", SomeModel)
            self.assertEqual(res, "норм")
            expected_calls = [
                call("abc123"),
            ]
            self.assertEqual(expected_calls, m_model_predict.mock_calls)

    @patch("model.SomeModel.predict")
    def test_predict_message_mood_corner_cases(self, m_model_predict):
        m_model_predict.side_effect = [0.3, 0.8]

        res = predict_message_mood("Какая-то строка", SomeModel)
        self.assertEqual(res, "норм")

        res = predict_message_mood("Еще одна строка", SomeModel)
        self.assertEqual(res, "норм")

        expected_calls = [call("Какая-то строка"), call("Еще одна строка")]
        self.assertEqual(expected_calls, m_model_predict.mock_calls)

    @patch("model.SomeModel.predict")
    def test_predict_message_mood_side_effect(self, m_model_predict):
        m_model_predict.side_effect = custom_prediction

        res = predict_message_mood("100 долларов", SomeModel)
        self.assertEqual(res, "неуд")

        res = predict_message_mood("В этой строке только буквы", SomeModel)
        self.assertEqual(res, "неуд")

        res = predict_message_mood("Pi is almost 3.14159265359", SomeModel)
        self.assertEqual(res, "норм")

        expected_calls = [
            call("100 долларов"),
            call("В этой строке только буквы"),
            call("Pi is almost 3.14159265359"),
        ]
        self.assertEqual(expected_calls, m_model_predict.mock_calls)


if __name__ == "__main__":
    unittest.main()

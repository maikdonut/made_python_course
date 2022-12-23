import unittest


class TestPartition(unittest.TestCase):
    def test_str_partition_unique_words(self):
        str1 = "Sky is blue".partition("is")
        self.assertEqual(str1, ("Sky ", "is", " blue"))

        str2 = "Яблоко от яблони".partition("от")
        self.assertEqual(str2, ("Яблоко ", "от", " яблони"))

        str3 = "Сегодня 19 декабря".partition("19")
        self.assertEqual(str3, ("Сегодня ", "19", " декабря"))

    def test_str_partition_not_unique_words(self):
        str1 = "B follows A, C follows B".partition("follows")
        self.assertEqual(str1, ("B ", "follows", " A, C follows B"))

        str2 = "so far so good".partition("so")
        self.assertEqual(str2, ("", "so", " far so good"))

        str3 = "Листья в поле пожелтели, и кружатся, и летят".partition(" и ")
        self.assertEqual(str3, ("Листья в поле пожелтели,", " и ", "кружатся, и летят"))

    def test_str_partition_no_sep_words(self):
        str1 = "He is a good artist".partition("bad")
        self.assertEqual(str1, ("He is a good artist", "", ""))

        str2 = "2 + 2 = 4".partition("5")
        self.assertEqual(str2, ("2 + 2 = 4", "", ""))

        str3 = "Euler number is almost 2.71828".partition("pi")
        self.assertEqual(str3, ("Euler number is almost 2.71828", "", ""))

    def test_str_partition_left_sep_words(self):
        str1 = "the best of the best".partition("the")
        self.assertEqual(str1, ("", "the", " best of the best"))

        str2 = "error code is 1122".partition("error")
        self.assertEqual(str2, ("", "error", " code is 1122"))

        str3 = "7 * 7 = 49".partition("7")
        self.assertEqual(str3, ("", "7", " * 7 = 49"))

    def test_str_partition_right_sep_words(self):
        str1 = "He has written his first book".partition("book")
        self.assertEqual(str1, ("He has written his first ", "book", ""))

        str2 = "Код от сейфа: 1234".partition("1234")
        self.assertEqual(str2, ("Код от сейфа: ", "1234", ""))

        str3 = "ln(e) = 1".partition("1")
        self.assertEqual(str3, ("ln(e) = ", "1", ""))


    def test_str_partition_sep_whole_word(self):
        str1 = "Indivisible string".partition("Indivisible string")
        self.assertEqual(str1, ("", "Indivisible string", ""))

        str2 = "Python".partition("Python")
        self.assertEqual(str2, ("", "Python", ""))

        str3 = "The last one".partition("The last one")
        self.assertEqual(str3, ("", "The last one", ""))

if __name__ == "__main__":
    unittest.main()

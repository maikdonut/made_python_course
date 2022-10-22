import unittest
from anagram import compare, find_anagrams


class TestAnagram(unittest.TestCase):
    def test_compare(self):
        arr1 = [1, 1, 2, 3, 5]
        arr2 = [2, 4, 6, 8, 10]
        arr3 = [2, 4, 6, 8, 10]
        arr4 = [0, 2, 4, 6, 8]
        self.assertFalse(compare(arr1, arr2, 5))
        self.assertTrue(compare(arr2, arr3, 5))
        self.assertFalse(compare(arr3, arr4, 5))

    def test_find_anagrams(self):
        text1 = "xyz zxy abc azyxbc"
        pattern1 = "xyz"
        res1 = find_anagrams(text1, pattern1)
        self.assertEqual(res1, [0, 4, 13])

        text2 = "cabXYZabcZYXbca"
        pattern2 = "abc"
        res2 = find_anagrams(text2, pattern2)
        self.assertEqual(res2, [0, 6, 12])

        text3 = "B BB BBB"
        pattern3 = "B"
        res3 = find_anagrams(text3, pattern3)
        self.assertEqual(res3, [0, 2, 3, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()

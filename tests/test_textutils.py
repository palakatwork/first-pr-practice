import unittest

from textutils import word_count


class WordCountTest(unittest.TestCase):
    def test_counts_words(self):
        self.assertEqual(word_count("one two three"), 3)

    def test_empty_string(self):
        self.assertEqual(word_count(""), 0)


if __name__ == "__main__":
    unittest.main()

import unittest

from textutils import slugify, word_count


class WordCountTest(unittest.TestCase):
    def test_counts_words(self):
        self.assertEqual(word_count("one two three"), 3)

    def test_empty_string(self):
        self.assertEqual(word_count(""), 0)


class SlugifyTest(unittest.TestCase):
    def test_lowercases_and_hyphenates(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_collapses_extra_whitespace(self):
        self.assertEqual(slugify("  Hello   big\tWorld  "), "hello-big-world")

    def test_empty_string(self):
        self.assertEqual(slugify(""), "")


if __name__ == "__main__":
    unittest.main()

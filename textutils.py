"""Small helpers for working with text."""


def word_count(text):
    """Return the number of words in ``text``."""
    return len(text.split())


def slugify(text):
    """Turn ``text`` into a lowercase, hyphen-separated slug.

    >>> slugify("Hello World")
    'hello-world'
    """
    return "-".join(text.lower().split())

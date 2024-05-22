import pytest

from assignment_2_1 import palindrome


@pytest.mark.parametrize(
    ("string", "start", "end", "expected"),
    [
        ("krk", 0, 3, True),
        ("krkavec", 0, 3, True),
        ("Celkem jednu sovu sam pan Knap ma suvo sundejme klec.", 0, 53, True),
        ("Kobyla ma maly bok", 0, 18, True),
        ("ABBA je moje oblibena skupina.", 0, 4, True),
        ("To neni mozny! Je blbej?", 15, 24, True),
        ("Baf! Lekl ses?", 0, 4, False),
        ("Nemas doma kladivo?", 11, 18, False),
        ("Lapal atom Ota", 0, 14, False),
        ("Lapal atom Ota", 5, 14, True),
        ("Popocatepetl je sopka v Mexiku", 0, 30, False),
    ]
)
def test_palindrome(string, expected, start, end):
    assert palindrome(string, start, end) == expected

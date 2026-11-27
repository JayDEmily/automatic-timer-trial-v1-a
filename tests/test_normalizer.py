import unittest
from normalizer import normalize


class NormalizeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize([]), [])

    def test_order_duplicates_and_case(self):
        self.assertEqual(normalize(["North", "west", "North"]), ["North", "west", "North"])

    def test_internal_whitespace(self):
        self.assertEqual(normalize(["a b", "C  d"]), ["a b", "C  d"])

    def test_trims_surrounding_whitespace(self):
        self.assertEqual(normalize(["  North ", "\twest\n", "\rEast\t"]), ["North", "west", "East"])

    def test_omits_blank_entries(self):
        self.assertEqual(normalize(["", " \t", " a ", "\n\r", "b", " "]), ["a", "b"])
        self.assertEqual(normalize(["", " ", "\t\n"]), [])

    def test_trimmed_duplicates_preserve_order(self):
        self.assertEqual(normalize([" z ", " a", "z\t", " a ", "z"]), ["z", "a", "z", "a", "z"])

    def test_trimming_preserves_case_and_internal_whitespace(self):
        self.assertEqual(normalize(["  A  b \t", "\tC\t D ", " eF "]), ["A  b", "C\t D", "eF"])

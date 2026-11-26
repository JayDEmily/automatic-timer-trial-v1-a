import unittest
from normalizer import normalize


class NormalizeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize([]), [])

    def test_order_duplicates_and_case(self):
        self.assertEqual(normalize(["North", "west", "North"]), ["North", "west", "North"])

    def test_internal_whitespace(self):
        self.assertEqual(normalize(["a b", "C  d"]), ["a b", "C  d"])

    def test_trims_edges(self):
        self.assertEqual(normalize(["  North  ", "\twest\n", "South"]), ["North", "west", "South"])

    def test_omits_blank_entries(self):
        self.assertEqual(normalize(["", "  ", "\t\n", " A ", "", " B", "   "]), ["A", "B"])
        self.assertEqual(normalize(["", "  ", "\t\n"]), [])

    def test_trim_preserves_order_duplicates_case_and_internal_whitespace(self):
        self.assertEqual(normalize([" North ", " west  wind ", "North", "  nORTH ", "C  d"]), ["North", "west  wind", "North", "nORTH", "C  d"])

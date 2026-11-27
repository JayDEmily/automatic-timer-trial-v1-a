import unittest
from normalizer import normalize


class NormalizeTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(normalize([]), [])

    def test_order_duplicates_and_case(self):
        self.assertEqual(normalize(["North", "west", "North"]), ["North", "west", "North"])

    def test_internal_whitespace(self):
        self.assertEqual(normalize(["a b", "C  d"]), ["a b", "C  d"])

    def test_trims_leading_and_trailing_whitespace(self):
        self.assertEqual(normalize(['  Alpha  ', '\tBeta\n']), ['Alpha', 'Beta'])

    def test_omits_blank_entries(self):
        self.assertEqual(normalize(['', ' \t\n', 'x', '', '\u2003']), ['x'])

    def test_preserves_order_and_duplicates_after_trimming(self):
        self.assertEqual(
            normalize([' North ', 'west', 'North', ' North\t']),
            ['North', 'west', 'North', 'North'],
        )

    def test_preserves_case_and_internal_whitespace_after_trimming(self):
        self.assertEqual(
            normalize(['  MiXeD  case\tText  ', '\ta b\n']),
            ['MiXeD  case\tText', 'a b'],
        )

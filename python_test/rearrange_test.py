from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase="Lovelace, Ada"
        expected="Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase=""
        expected=""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_names(self):
        testcase="Rinson, Davis I."
        expected="Davis I. Rinson"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase="Rinson"
        expected="Rinson"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()
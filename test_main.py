from unittest import TestCase
from main import replace


class Test(TestCase):

    def test_replace_case_1(self):
        self.assertEqual(replace('123 abcd*3'), '123 bcde*3', 'Invalid output')

    def test_replace_case_2(self):
        self.assertEqual(replace('**Casa 52'), '**Dbtb 52', 'Invalid output')

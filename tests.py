import unittest
import json

from pprint_json import prettify_json as p, load_json_input as l


class TestJsonOutputs(unittest.TestCase):

    def test_long_json(self):
        '''Testing long json file'''
        actual = l('./testcases/actual/long.json')
        actual_pretty =  p(actual)

        with open('./testcases/expected/long.txt', 'r', encoding='utf-8') as expected:
            expected_pretty = expected.read()
            self.assertEqual(actual_pretty, expected_pretty, 'Json dumps are unmatching')

    def test_short_json(self):
        actual = l('./testcases/actual/short.json')
        actual_pretty =  p(actual)

        with open('./testcases/expected/short.txt', 'r', encoding='utf-8') as expected:
            expected_pretty = expected.read()
            self.assertEqual(actual_pretty, expected_pretty, 'Json dumps are unmatching')


if __name__ == '__main__':
    unittest.main()

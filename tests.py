import unittest
import json

from pprint_json import pretty_print_json as ppj
import json


class TestJsonOutputs(unittest.TestCase):

    def test_short_json(self):
        '''Testing long json file'''
        with open('./testcases/actual/long.json', 'r', encoding='utf-8') as actual:
            actual_long =  json.load(actual)
        with open('./testcases/expected/long.json', 'r', encoding='utf-8') as expected:
            expected_long = json.load(expected)
        
        self.assertEqual(actual_long, expected_long, 'Json files are unmatching')
    
    def test_long_json(self):
        '''Testing short json file'''
        with open('./testcases/actual/short.json', 'r', encoding='utf-8') as actual:
            actual_short =  json.load(actual)
        with open('./testcases/expected/short.json', 'r', encoding='utf-8') as expected:
            expected_short = json.load(expected)

        self.assertEqual(actual_short, expected_short, 'Json files are unmatching')

if __name__ == '__main__':
    unittest.main()
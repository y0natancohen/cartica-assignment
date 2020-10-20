import unittest

from reachable import is_end_reachable
from input import get_list_from_file, InvalidInputError


class ReachableTest(unittest.TestCase):
    def test_reachable(self):

        files = [
            ('test/path.json', True),
            ('test/path.tsv', True),
            ('test/path.csv', True),

            ('test/no_path.tsv', False),
            ('test/no_path.csv', False),
            ('test/no_path.json', False),

            ('test/long.json', True),
            ('test/very_long.json', True),
            ('test/very_long_no_path.json', False),
        ]

        for file_name, result in files:
            try:
                int_list = get_list_from_file(file_name)
                self.assertEqual(is_end_reachable(int_list), result,
                                 'file {} result should be {}'.format(file_name, result))
            except InvalidInputError as e:
                print('Error: file {} has invalid input: {}'.format(file_name, e))

    def test_bad_input(self):
        j_files = [
            'test/bad_input.json',
            'test/bad_input_2.json',
        ]
        for file_name in j_files:
            int_list = get_list_from_file(file_name)
            self.assertRaises(InvalidInputError, is_end_reachable, int_list)

        sv_files = [
            'test/bad_input.csv',
            'test/bad_input.tsv',
        ]
        for file_name in sv_files:
            self.assertRaises(InvalidInputError, get_list_from_file, file_name)


if __name__ == '__main__':
    unittest.main()

import unittest

from cli import parser


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = parser

    def test_timeout(self):
        parsed = self.parser.parse_args(['-u', 'http://example.com?id=3',
                                         '--timeout', '10'])
        self.assertEqual(parsed.timeout, 10)

    def test_method_type(self):
        parsed = self.parser.parse_args(['-u', 'http://example.com?id=3',
                                         '--method', 'PATCH'])
        self.assertEqual(parsed.method, "PATCH")


if __name__ == '__main__':
    unittest.main()

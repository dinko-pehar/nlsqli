import unittest

from utils import URLParserType


class UtilsTest(unittest.TestCase):

    def test_url_parser_type_class(self):

        url_1 = "http://localhost/sqli/?id=3&x=4"
        url_1_parsed = URLParserType(url_1)

        # Should be dictionary.
        self.assertDictEqual(url_1_parsed.qs, {'id': '3', 'x': '4'})
        # Should contain 2 query attributes
        self.assertEqual(len(url_1_parsed.qs), 2)
        # URL shouldn't contain query string.
        self.assertNotIn("?id=3&x=4", url_1_parsed.url)

        url_2 = "http://localhost/sqli/?"
        url_2_parsed = URLParserType(url_2)

        self.assertEqual(len(url_2_parsed.qs), 0)
        self.assertNotIn("?", url_2_parsed.url)


if __name__ == '__main__':
    unittest.main()

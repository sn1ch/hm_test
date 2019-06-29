import unittest
from hm_tests.task2 import yandex_translate_api


class Test_yandex_translate_api(unittest.TestCase):

    def test_translate_it(self):
        text = 'привет'
        expected_response = '{"code":200,"lang":"ru-fr","text":["salut"]}'
        self.assertEqual(yandex_translate_api.translate_it(text, 'ru', 'fr'), expected_response)

    def test_translate_max_line_error(self):
        text = 'a' * 11000
        expected_response = '{"code":413,"message":"The text size exceeds the maximum"}'
        self.assertEqual(yandex_translate_api.translate_it(text, 'ru', 'en'), expected_response)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch
from hm_tests.task1 import secretary
import json


class Test_secretaty(unittest.TestCase):
    def setUp(self):
        with open('fixture/directories.json', 'r', encoding='UTF-8') as file:
            self.directories = json.load(file)
        with open('fixture/documents.json', 'r', encoding='UTF-8') as file:
            self.documents = json.load(file)

    def test_full_documents_list_return_none(self):
        self.assertEqual(secretary.full_documents_list(self.documents), None)

    def test_find_people_equal(self):
        self.assertEqual(secretary.find_people(self.documents, '11-2'), 'Геннадий Покемонов')

    def test_find_people_result(self):
        self.assertMultiLineEqual(secretary.find_people(self.documents, '11-2'), 'Геннадий Покемонов')

    def test_move_units_result(self):
        self.assertDictEqual(secretary.move_units(self.directories, '11-2', '4'),
                             {'1': ['2207 876234'], '2': ['10006'], '3': [], '4': ['11-2']})

    def test_del_units_result(self):
        output = ({'1': ['2207 876234'], '2': ['10006'], '3': []}, [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ])
        self.assertEqual(secretary.del_units(self.documents, self.directories, '11-2'),
                         output)

    def test_storage_place_type(self):
        self.assertMultiLineEqual(secretary.storage_place(self.directories, '11-2'), '1')

    def test_storage_place_negative_result(self):
        self.assertNotEqual(secretary.storage_place(self.directories, '11-2'), '2')

    @patch('builtins.input', lambda *args: 'test_write')
    def test_add_unit(self):
        output = ([{'name': 'Василий Гупкин', 'number': '2207 876234', 'type': 'passport'},
                   {'name': 'Геннадий Покемонов', 'number': '11-2', 'type': 'invoice'},
                   {'name': 'Аристарх Павлов', 'number': '10006', 'type': 'insurance'},
                   {'name': 'test_write', 'number': 'test_write', 'type': 'test_write'}],
                  {'1': ['2207 876234', '11-2'],
                   '2': ['10006'],
                   '3': [],
                   'test_write': ['test_write']})
        self.assertEqual(secretary.add_unit(self.documents, self.directories), output)


if __name__ == '__main__':
    unittest.main()

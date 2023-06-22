import unittest
from src.utils import json_to_dict, dict_to_json, json_parser


class TestUtils(unittest.TestCase):

    def test_json_to_dict(self):
        json_data = '{"key1": "value1", "key2": "value2"}'
        expected_dict = {"key1": "value1", "key2": "value2"}
        result_dict = json_to_dict(json_data)
        self.assertEqual(result_dict, expected_dict)

    def test_dict_to_json(self):
        dict_data = {"key1": "value1", "key2": "value2"}
        expected_json = '{"key1": "value1", "key2": "value2"}'
        result_json = dict_to_json(dict_data)
        self.assertEqual(result_json, expected_json)

    def test_json_parser(self):
        data = '{"task_text": "Напиши функцию", "task_answer": "def my_func(): pass", "task_status": 0}'
        expected_result = 'Вот текст задачи: Напиши функцию Вот моё решение: def my_func(): pass. Помоги!'
        result = json_parser(data)
        self.assertEqual(result, expected_result)

    def test_json_parser_with_exception(self):
        data = '{"task_text": "Напиши функцию", "task_answer": "def my_func(): pass", "task_status": 1}'
        with self.assertRaises(ValueError) as context:
            json_parser(data)
        self.assertTrue('Задача была решена' in str(context.exception))


if __name__ == '__main__':
    unittest.main()

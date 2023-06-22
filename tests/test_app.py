import unittest
import json

from app import app


class TestServer(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_server_response(self):
        # Тестирование ответа сервера
        response = self.app.post('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('hello', response.get_data(as_text=True))

    def test_post_json(self):
        # Отправка POST-запроса с данными JSON
        data = {
            "user_id": 0,
            "problem_id": 0,
            "task_text": "# напишите функцию, которая принимает список из уникальных элементов, кроме одного, который присутствует 2 раза, и возвращает часть списка, которая находится между этими повторяющимися элементами (не включая).",
            "task_answer": "def remove_between_1(l): index = [i for i, x in enumerate(l) if l.count(x)>1] return l[index[0]: index[1]]",
            "task_status": 0
        }

        response = self.app.post(
            '/api', data=json.dumps(data), content_type='application/json')

        # Проверка кода состояния ответа
        self.assertEqual(response.status_code, 200)

        # Проверка содержимого ответа
        response_data = json.loads(response.get_data(as_text=True))
        string = 'индекс'

        self.assertTrue(string in str(response_data))

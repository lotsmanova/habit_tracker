from rest_framework import status

from base.tests import BaseTestCase


class UserTestCase(BaseTestCase):

    def setUp(self) -> None:
        super().setUp()

    def test_create_user(self):
        """Тестирование создания пользователя"""

        data = {
            'email': 'test3@mail.ru',
            'password': 'test1',
            'chat_id': '1727774413'
        }

        response = self.client.post(
            '/users/user/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 8, 'username': None, 'password': 'test1', 'email': 'test3@mail.ru', 'phone': None,
             'chat_id': '1727774413'}
        )

    def test_list_user(self):
        """Тестирование вывода списка пользователей"""
        response = self.client.get(
            '/users/user/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{'id': 10, 'username': None, 'email': 'test@mail.ru', 'phone': None, 'chat_id': '1727774413'}]
        )

    def test_retrieve_user(self):
        """Тестирование вывода одного пользователя"""

        response = self.client.get(
            f'/users/user/{self.user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 11, 'username': None, 'email': 'test@mail.ru', 'phone': None, 'chat_id': '1727774413'}
        )

    def test_update_user(self):
        """Тестирование обновления пользователя"""

        data = {'email': 'test_update@mail.ru'}
        response = self.client.patch(
            f'/users/user/{self.user.id}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 12, 'username': None, 'email': 'test_update@mail.ru', 'phone': None, 'chat_id': '1727774413'}
        )

    def test_delete_user(self):
        """Тестирование удаления пользователя"""

        response = self.client.delete(
            f'/users/user/{self.user.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

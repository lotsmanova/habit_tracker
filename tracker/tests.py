from django.urls import reverse
from rest_framework import status
from base.tests import BaseTestCase


class TrackerTestCase(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()

    def test_create_habit(self):
        """Тестирование создания привычки"""
        data = {
            'user': self.user.id,
            'place': 'place',
            'time': '19:00:00',
            'action': 'action',
            'time_to_complete': '00:00:30'
        }

        response = self.client.post(
            reverse('tracker:habit_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 2, 'place': 'place', 'time': '19:00:00', 'action': 'action', 'is_good_habit': False,
             'frequency': 'Ежедневно', 'award': None, 'time_to_complete': '00:00:30', 'is_public': False,
             'time_last_send': None, 'user': 1, 'related_habit': None}
        )

    def test_list_habit(self):
        """Тестирование списка привычек"""
        response = self.client.get(
            reverse('tracker:habit_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['results'],
            [{'id': 4, 'place': 'Test place', 'time': '16:10:00',
              'action': 'Test action', 'is_good_habit': False,
              'frequency': 'Ежедневно', 'award': None, 'time_to_complete': '00:01:00', 'is_public': False,
              'time_last_send': None, 'user': 3, 'related_habit': None}]
        )

    def test_list_public_habit(self):
        """Тестирование спика публичных привычек"""
        response = self.client.get(
            reverse('tracker:habit_public')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['results'],
            []
        )

    def test_retrieve_habit(self):
        """Тестирование вывода одной привычки"""
        response = self.client.get(
            reverse('tracker:habit_retrieve', kwargs={'pk': self.habit.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 6, 'place': 'Test place', 'time': '16:10:00',
             'action': 'Test action', 'is_good_habit': False,
             'frequency': 'Ежедневно', 'award': None, 'time_to_complete': '00:01:00', 'is_public': False,
             'time_last_send': None, 'user': 5, 'related_habit': None}
        )

    def test_delete_habit(self):
        """Тестирование удаления привычки"""
        response = self.client.delete(
            reverse('tracker:habit_delete', kwargs={'pk': self.habit.id})
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_update_habit(self):
        """Тестирование обновления привычки"""
        data = {'action': 'action update'}
        response = self.client.patch(
            reverse('tracker:habit_update', kwargs={'pk': self.habit.id}),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 7, 'place': 'Test place', 'time': '16:10:00',
             'action': 'action update', 'is_good_habit': False,
             'frequency': 'Ежедневно', 'award': None, 'time_to_complete': '00:01:00', 'is_public': False,
             'time_last_send': None, 'user': 6, 'related_habit': None}
        )

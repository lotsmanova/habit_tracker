from django.urls import reverse
from rest_framework.test import APITestCase

from tracker.models import Habits
from users.models import User


class BaseTestCase(APITestCase):
    email = 'test@mail.ru'
    password = '12345'
    chat_id = '1727774413'

    def setUp(self) -> None:
        self.user = User.objects.create(
            email=self.email,
            chat_id=self.chat_id
        )

        self.user.set_password(self.password)
        self.user.save()

        response = self.client.post(
            reverse('users:token_obtain_pair'),
            {
                'email': self.email,
                'chat_id': self.chat_id,
                'password': self.password
            }
        )

        self.token = response.json().get('access')

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        self.habit = Habits.objects.create(
            user=self.user,
            place='Test place',
            time='16:10:00',
            action='Test action',
            time_to_complete='00:01:00'
        )

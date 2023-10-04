from datetime import timedelta

import requests
from django.conf import settings
from django.utils import timezone

from tracker.models import Habits


def send_notification_tg(*args, **kwargs):
    now = timezone.now()
    habits = Habits.objects.filter(time__lte=now + timedelta(minutes=5))
    send_url = f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage'
    for habit in habits:
        requests.post(
            send_url,
            json={
                "chat_id": habit.user.chat_id,
                "text": f'В {habit.time} вы хотели начать {habit.action} в {habit.place}'
            }
        )


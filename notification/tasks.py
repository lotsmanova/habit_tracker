from datetime import timedelta, datetime
import requests
from django.conf import settings
from django.utils import timezone
from rest_framework.response import Response

from tracker.models import Habits


def send_notification_tg(*args, **kwargs):
    now = datetime.now()
    habits = Habits.objects.all()
    send_url = f'https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage'

    for habit in habits:
        habit_time = datetime.combine(datetime.today(), habit.time)

        if ((habit.frequency == 'one daily' and (now - habit.time_last_send) > timedelta(days=1))
                or ((habit.frequency == 'two daily' and (now - habit.time_last_send) > timedelta(days=2))
                    or (habit.frequency == 'three daily' and (now - habit.time_last_send) > timedelta(days=3)))
                or (habit.frequency == 'four daily' and (now - habit.time_last_send) > timedelta(days=4))
                or (habit.frequency == 'five daily' and (now - habit.time_last_send) > timedelta(days=5))
                or (habit.frequency == 'six daily' and (now - habit.time_last_send) > timedelta(days=6))
                or (habit.frequency == 'seven daily' and (now - habit.time_last_send) > timedelta(days=7))):

            if now - timedelta(minutes=30) < habit_time < now + timedelta(minutes=30):

                response = requests.post(
                    send_url,
                    json={
                        "chat_id": habit.user.chat_id,
                        "text": f'В {habit.time} вы хотели начать {habit.action} в {habit.place}'
                    }
                )
                return Response(response.status_code)

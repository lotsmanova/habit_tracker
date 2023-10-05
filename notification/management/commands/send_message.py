from django.core.management import BaseCommand

from notification.tasks import send_notification_tg


class Command(BaseCommand):
    """Кастомная команда для отправки уведомлений в телеграмм"""
    def handle(self, *args, **options):

        send_notification_tg()

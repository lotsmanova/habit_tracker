from django.conf import settings
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=settings.ADMIN_EMAIL,
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True
        )
        user.set_password(settings.ADMIN_PASSWORD)
        user.save()

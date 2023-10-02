from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Habits(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.CharField(max_length=150, verbose_name='место исполнения привычки')
    time = models.DateTimeField(verbose_name='дата и время выполнения привычки')
    action = models.CharField(max_length=150, verbose_name='действие привычки')
    is_good_habit = models.BooleanField(verbose_name='признак приятной привычки', default=False, **NULLABLE)
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    frequency = models.CharField(max_length=100, verbose_name='периодичность', default='Ежедневно')
    award = models.CharField(max_length=200, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(verbose_name='время на выполнение')
    is_public = models.BooleanField(verbose_name='признак публизности', default=False)


    def __str__(self):
        return f'{self.action} - {self.time} - {self.place}'


    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

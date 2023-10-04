import datetime
from datetime import timedelta

from rest_framework import serializers

from tracker.models import Habits


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'

    def validate(self, data):

        if data.get('related_habit') and data.get('award'):
            raise serializers.ValidationError({
                'message_error': "Нельзя одновременно выбрать 'Связанную привычку' и 'Вознаграждение'. Выберите что-то одно."
            })

        elif data.get('time_to_complete').minute >= 2:
            raise serializers.ValidationError({
                'message_error': "Время выполнения должно быть не больше 120 секунд"
            })

        elif data.get('frequency') in ['неделя', 'месяц'] or int(data.get('frequency')) > 7:
            raise serializers.ValidationError({
                'message_error': "Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
            })

        elif data.get('related_habit'):
            if not data.get('related_habit').is_good_habit:
                raise serializers.ValidationError({
                    'message_error': "В связанные привычки могут попадать только привычки с признаком приятной привычки."
                })

        elif data.get('is_good_habit'):
            if data.get('related_habit') or data.get('award'):
                raise serializers.ValidationError({
                    'message_error': "Нельзя выбрать 'Связанную привычку' и 'Вознаграждение' для приятной привычки."
                })







        return data

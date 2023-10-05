from rest_framework import serializers
from tracker.models import Habits

FREQUENCIES = ['Ежедневно', 'Раз в два дня', 'Раз в три дня', 'Раз в четыре дня',
               'Раз в пять дней', 'Раз в шесть дней', 'Раз в семь дней']


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор привычки"""
    class Meta:
        model = Habits
        fields = '__all__'


class HabitCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания привычки"""
    class Meta:
        model = Habits
        fields = '__all__'

    def validate(self, data):

        if data.get('related_habit') and data.get('award'):
            raise serializers.ValidationError({
                'message_error': "Нельзя одновременно выбрать 'Связанную привычку' "
                                 "и 'Вознаграждение'. Выберите что-то одно."
            })

        elif data.get('time_to_complete').minute >= 2:
            raise serializers.ValidationError({
                'message_error': "Время выполнения должно быть не больше 120 секунд"
            })

        elif data.get('frequency') and data.get('frequency') not in FREQUENCIES:
            raise serializers.ValidationError({
                'message_error': "Нельзя выполнять привычку реже, чем 1 раз в 7 дней."
            })

        elif data.get('related_habit'):
            if not data.get('related_habit').is_good_habit:
                raise serializers.ValidationError({
                    'message_error': "В связанные привычки могут попадать только привычки "
                                     "с признаком приятной привычки."
                })

        elif data.get('is_good_habit'):
            if data.get('related_habit') or data.get('award'):
                raise serializers.ValidationError({
                    'message_error': "Нельзя выбрать 'Связанную привычку' и 'Вознаграждение' для приятной привычки."
                })
        return data

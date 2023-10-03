from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from tracker.models import Habits
from tracker.serializers import HabitSerializer


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitsListAPIView(generics.ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitsUpdateAPIView(generics.UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitsDestroyAPIView(generics.DestroyAPIView):
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated]

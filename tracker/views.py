from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from tracker.models import Habits
from tracker.paginators import ListPaginator
from tracker.serializers import HabitSerializer, HabitCreateSerializer
from users.permissions import IsOwner


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitsListAPIView(generics.ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = ListPaginator

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)



class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsUpdateAPIView(generics.UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsDestroyAPIView(generics.DestroyAPIView):
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitListPublicAPIView(generics.ListAPIView):
    queryset = Habits.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = ListPaginator


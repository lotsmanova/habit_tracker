from django.urls import path

from tracker.apps import TrackerConfig
from tracker.views import HabitsCreateAPIView, HabitsListAPIView, HabitsRetrieveAPIView, HabitsUpdateAPIView, HabitsDestroyAPIView

app_name = TrackerConfig.name


urlpatterns = [
    path('habit/create/', HabitsCreateAPIView.as_view(), name='habit_create'),
    path('habit/', HabitsListAPIView.as_view(), name='habit_list'),
    path('habit/<int:pk>/', HabitsRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habit/update/<int:pk>/', HabitsUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitsDestroyAPIView.as_view(), name='habit_delete')
]

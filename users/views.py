from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsOwner
from users.serializers import UserListSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """CRUD для пользователя"""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    default_serializer = UserListSerializer
    serializers = {
        'create': UserSerializer,
        'retrieve': UserListSerializer,
        'update': UserListSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'retrieve']:
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()

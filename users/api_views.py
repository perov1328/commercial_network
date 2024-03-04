from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAdminUser
from users.models import User
from users.permissions import IsUser
from users.serializers import UserSerializer, UserViewSerializer


class UserCreateAPIView(CreateAPIView):
    """
    Контроллер для создания сущности моедли Пользователя
    """
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотора конкретной сущности модели Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserViewSerializer
    permission_classes = [IsUser]


class UserUpdateAPIView(UpdateAPIView):
    """
    Контроллер для обновления сущности модели Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUser]


class UserDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаления сущности модели Пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUser | IsAdminUser]

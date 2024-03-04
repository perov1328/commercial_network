from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from net.filters import NetElementFilter
from net.models import NetElement
from net.serializers import NetElementListSerializer, NetElementRetriveSerializer, NetElementCreateSerializer
from net.paginators import NetElementPagination
from net.services import hierarchy_level_calc
from rest_framework.permissions import IsAuthenticated


class NetElementListAPIView(ListAPIView):
    """
    Контроллер для просмотра списка всех Элементов Сети
    """
    queryset = NetElement.objects.all()
    serializer_class = NetElementListSerializer
    pagination_class = NetElementPagination
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = NetElementFilter


class NetElementRetriveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотра информации о конкретном Элементе Сети
    """
    queryset = NetElement.objects.all()
    serializer_class = NetElementRetriveSerializer
    permission_classes = [IsAuthenticated]


class NetElementDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаления конкретного Элемента Сети
    """
    queryset = NetElement.objects.all()
    serializer_class = NetElementListSerializer
    permission_classes = [IsAuthenticated]


class NetElementCreateAPIView(CreateAPIView):
    """
    Контроллер для создания Элемента Сети
    """
    queryset = NetElement.objects.all()
    serializer_class = NetElementCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        hierarchy_level_calc(self, serializer)


class NetElementUpdateAPIView(UpdateAPIView):
    queryset = NetElement.objects.all()
    serializer_class = NetElementCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        hierarchy_level_calc(self, serializer)

from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from products.models import Product
from products.serializers import ProductSerializer
from products.paginators import ProductPagination
from rest_framework.permissions import IsAuthenticated


class ProductListAPIView(ListAPIView):
    """
    Контроллер для просмотра списка всех Товаров
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    permission_classes = [IsAuthenticated]


class ProductCreateAPIView(CreateAPIView):
    """
    Контроллер для создания сущности Товара
    """
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductUpdateAPIView(UpdateAPIView):
    """
    Контроллер для обновления информации по конкретному Товару
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductDeleteAPIView(DestroyAPIView):
    """
    Контроллер для удаления конкретного товара
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class ProductRetrieveAPIView(RetrieveAPIView):
    """
    Контроллер для просмотра информации о конкретном товаре
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

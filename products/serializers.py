from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Продукта
    """
    class Meta:
        model = Product
        fields = ('id', 'name', 'model', 'release_date',)

from rest_framework import serializers
from net.models import NetElement
from net.validators import provider_check


class NetElementListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для вывода списка моделей Элементов Сети
    """

    class Meta:
        model = NetElement
        fields = ('id', 'title', 'business_form',
                  'email', 'country', 'city', 'street', 'house_number',
                  'provider', 'debt',)


class NetElementRetriveSerializer(serializers.ModelSerializer):
    """
    Сериализатор для вывода информации о конкретном Элементе Сети
    """

    class Meta:
        model = NetElement
        fields = ('id', 'title', 'business_form', 'hierarchy_level',
                  'email', 'country', 'city', 'street', 'house_number',
                  'provider', 'products', 'debt', 'date_of_creation',)


class NetElementCreateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для создания модели Элемента Сети
    """
    hierarchy_level = serializers.IntegerField(read_only=True)
    debt = serializers.DecimalField(max_digits=20, decimal_places=2, read_only=True)

    class Meta:
        model = NetElement
        fields = ('id', 'title', 'business_form', 'hierarchy_level',
                  'email', 'country', 'city', 'street', 'house_number',
                  'provider', 'products', 'debt',)
        validators = [
            provider_check(business_form='business_form', provider='provider')
        ]

from rest_framework.serializers import ValidationError


def hierarchy_level_calc(self, serializer):
    """
    Определение уровня иерархии у Элемента Сети
    """

    data = serializer.validated_data

    # Определение уровня иерархии если Элемент Сети является заводом
    if data['business_form'] == 'Factory':
        data['hierarchy_level'] = 0

    # Определение уровня иерархии если Элемент Сети не является заводом
    else:
        provider = data.get('provider')

        # Определение есть ли поставщик у данной модели
        if provider:
            provider_level = provider.hierarchy_level

            # Проверка что уровень иерархии не может быть больше 2 (т.к. отсчет с 0)
            if provider_level >= 2:
                raise ValidationError("Уровень иерархиии не может быть больше 2.")

            data['hierarchy_level'] = provider_level + 1

        else:
            data['hierarchy_level'] = 1

    serializer.save()


def clear_debt(modeladmin, request, queryset):
    """
    Функция для очистики задолженности перед поставщиком
    """
    queryset.update(debt=0)


clear_debt.short_description = 'Очистить задолженность'

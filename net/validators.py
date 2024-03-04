from rest_framework.serializers import ValidationError


class provider_check:
    """
    Валидатор для проверки поставщика у Завода
    """
    def __init__(self, business_form, provider):
        self.business_form = business_form
        self.provider = provider

    def __call__(self, value):
        business_form = value.get(self.business_form)
        provider = value.get(self.provider)
        if business_form == 'Factory' and provider:
            raise ValidationError("У завода не может быть поставщика")

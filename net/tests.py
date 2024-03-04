from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from users.models import User


class NetElementTestCase(APITestCase):
    """
    Тестирование для модели Элементо Сети
    """
    def setUp(self):
        self.user = User.objects.create(
            email='test1@yandex.ru',
            password='test12345'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_provider_check(self):
        """
        Тест для проверки что у Завода не может быть поставщика
        """
        data = {
            "title": "test",
            "business_form": "Factory",
            "email": "test@mail.ru",
            "country": "RU",
            "city": "Moscow",
            "street": "Red",
            "house_number": "1"
        }
        response = self.client.post(
            reverse('net:net_create'),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        data_bad = {
            "title": "test_bad",
            "business_form": "Factory",
            "email": "test_bad@mail.ru",
            "country": "RU",
            "city": "Moscow",
            "street": "Red",
            "house_number": "2",
            "provider": 1
        }
        response_bad = self.client.post(
            reverse('net:net_create'),
            data=data_bad
        )
        self.assertEqual(
            response_bad.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_hierarchy_level_calc(self):
        """
        Тест для расчет уровня иерархии
        """

        data = {
            "title": "test",
            "business_form": "Factory",
            "email": "test@mail.ru",
            "country": "RU",
            "city": "Moscow",
            "street": "Red",
            "house_number": "1"
        }
        response = self.client.post(
            reverse('net:net_create'),
            data=data
        )
        self.assertEqual(
            response.data['hierarchy_level'],
            0
        )

        data_retail = {
            "title": "test_ret",
            "business_form": "Retail",
            "email": "test_ret@mail.ru",
            "country": "RU",
            "city": "Moscow",
            "street": "Red",
            "house_number": "1",
            "provider": 1
        }
        response_ret = self.client.post(
            reverse('net:net_create'),
            data=data_retail
        )
        self.assertEqual(
            response_ret.data['hierarchy_level'],
            1
        )

        data_entrepreneur = {
            "title": "test_ent",
            "business_form": "Entrepreneur",
            "email": "test_ent@mail.ru",
            "country": "RU",
            "city": "Moscow",
            "street": "Red",
            "house_number": "1",
            "provider": 2
        }
        response_ent = self.client.post(
            reverse('net:net_create'),
            data=data_entrepreneur
        )
        self.assertEqual(
            response_ent.data['hierarchy_level'],
            2
        )

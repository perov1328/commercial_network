from django.db import models
from net.constants import BUSINESS_FORM, NULLABLE
from products.models import Product


class NetElement(models.Model):
    """
    Модель Элементов Сети
    """
    title = models.CharField(max_length=100, verbose_name='Название')
    business_form = models.CharField(max_length=15, choices=BUSINESS_FORM, verbose_name='Форма ведения бизнеса')
    hierarchy_level = models.IntegerField(**NULLABLE, verbose_name='Уровень элемента сети')
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house_number = models.CharField(max_length=50, verbose_name='Номер дома')
    provider = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Поставщик')
    products = models.ManyToManyField(Product, **NULLABLE, verbose_name='Продукты',)
    debt = models.DecimalField(max_digits=20, decimal_places=2, **NULLABLE, verbose_name='Задолженность')
    date_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'{self.title} ({self.country}) - {self.business_form}'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Элемент сети'
        verbose_name_plural = 'Элементы сети'

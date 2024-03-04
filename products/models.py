from django.db import models


class Product(models.Model):
    """
    Модель продукта
    """
    name = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=20, verbose_name='Модель')
    release_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода продукта на рынок')

    def __str__(self):
        """
        Возвращение строкового представления объекта
        """
        return f'{self.name} - {self.model}'

    class Meta:
        """
        Настройки для наименования объекта/объектов
        """
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

# Generated by Django 5.0.2 on 2024-03-01 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('business_form', models.CharField(choices=[('Factory', 'Factory'), ('Retail', 'Retail'), ('Entrepreneur', 'Entrepreneur')], max_length=15, verbose_name='Форма ведения бизнеса')),
                ('hierarchy_level', models.IntegerField(blank=True, null=True, verbose_name='Уровень элемента сети')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('street', models.CharField(max_length=50, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=50, verbose_name='Номер дома')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True, verbose_name='Задолженность')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='net.netelement', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'Элемент сети',
                'verbose_name_plural': 'Элементы сети',
            },
        ),
    ]
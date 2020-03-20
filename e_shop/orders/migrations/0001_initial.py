# Generated by Django 3.0.4 on 2020-03-20 11:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Полная цена')),
                ('status', models.CharField(choices=[('new', 'Новый заказ'), ('in_process', 'Заказ в процессе обработки'), ('renouncement', 'Заказ отклонен'), ('complete', 'Заказ выполнен '), ('?', 'Не получен ответ пользователя')], default='new', max_length=30, verbose_name='Статус')),
            ],
        ),
    ]

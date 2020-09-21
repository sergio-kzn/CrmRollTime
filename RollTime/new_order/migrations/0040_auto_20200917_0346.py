# Generated by Django 3.1 on 2020-09-17 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0039_auto_20200917_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_learning_from',
            field=models.CharField(choices=[(2, 'Сайт rolltime16.ru'), (3, 'Агрегаторы yandex или delivery')], max_length=100, verbose_name='Узнали из'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_payment',
            field=models.CharField(choices=[(2, 'Нал.'), (3, 'Б / нал.'), (4, 'Агрегатор')], max_length=100, verbose_name='Оплата'),
        ),
    ]
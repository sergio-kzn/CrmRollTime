# Generated by Django 3.1 on 2020-09-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0046_auto_20200917_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_person',
            field=models.CharField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15')], max_length=10, verbose_name='Приборы'),
        ),
    ]
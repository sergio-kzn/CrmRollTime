# Generated by Django 3.1 on 2020-09-13 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0016_auto_20200913_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_items',
            field=models.JSONField(blank=True, verbose_name='Товары'),
        ),
    ]

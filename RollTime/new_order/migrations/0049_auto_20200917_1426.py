# Generated by Django 3.1 on 2020-09-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0048_auto_20200917_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер заказа'),
        ),
    ]

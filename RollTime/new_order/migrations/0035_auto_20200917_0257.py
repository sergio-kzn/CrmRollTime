# Generated by Django 3.1 on 2020-09-16 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0034_auto_20200917_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_sale',
            field=models.CharField(choices=[(6, '-10%'), (10, '-100%'), (7, '-20%'), (3, '-3%'), (8, '-30%'), (4, '-5%'), (9, '-50%'), (5, '-7%'), (1, 'Без скидки'), (2, 'Суммой')], default='1', max_length=10, verbose_name='Скидка'),
        ),
    ]
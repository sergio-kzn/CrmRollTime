# Generated by Django 3.1 on 2020-09-17 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0036_auto_20200917_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_marks',
            field=models.CharField(choices=[(2, 'Доставка'), (3, 'С собой'), (4, 'В зале'), (1, 'x')], default=(1, 'x'), max_length=100, verbose_name='Отметки'),
        ),
    ]
# Generated by Django 3.1 on 2020-09-11 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0006_auto_20200911_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_order.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_order.color'),
        ),
    ]

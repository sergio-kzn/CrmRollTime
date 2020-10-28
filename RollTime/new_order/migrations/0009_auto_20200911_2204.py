# Generated by Django 3.1 on 2020-09-11 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0008_auto_20200911_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_color',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='new_order.color'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
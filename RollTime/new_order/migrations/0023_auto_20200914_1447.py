# Generated by Django 3.1 on 2020-09-14 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0022_auto_20200914_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'Филиал', 'verbose_name_plural': 'Филиалы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['category_sort'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'Цвет', 'verbose_name_plural': 'Цвета'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AddField(
            model_name='branch',
            name='branch_default',
            field=models.BooleanField(default=False, verbose_name='По умолчанию'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_order.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='new_order.color', verbose_name='Цвет'),
        ),
    ]

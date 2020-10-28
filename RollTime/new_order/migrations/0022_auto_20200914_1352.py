# Generated by Django 3.1 on 2020-09-14 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0021_auto_20200914_1336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='category',
            name='category_sort',
            field=models.IntegerField(default=0, verbose_name='Порядок'),
        ),
    ]

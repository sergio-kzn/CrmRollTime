# Generated by Django 3.1 on 2020-09-14 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0024_learningfrom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_learning_from',
            field=models.CharField(blank=True, choices=[{'id': 1, 'learning_from_name': 'Сайт rolltime16.ru'}, {'id': 2, 'learning_from_name': 'Агрегаторы yandex или delivery'}], max_length=100, verbose_name='Узнали из'),
        ),
    ]
# Generated by Django 3.1 on 2020-09-13 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0013_item_item_show'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_client',
        ),
        migrations.AddField(
            model_name='order',
            name='order_certificate',
            field=models.CharField(blank=True, max_length=100, verbose_name='Сертификат'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_client_name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Имя Клиента'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_client_phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Телефон Клиента'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_learning_from',
            field=models.CharField(blank=True, max_length=100, verbose_name='Узнали из'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(default=0, verbose_name='Номер заказа'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_person',
            field=models.IntegerField(default=1, verbose_name='Приборы'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_sale',
            field=models.IntegerField(default=0, verbose_name='Скидка'),
        ),
    ]
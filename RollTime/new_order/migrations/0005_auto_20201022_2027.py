# Generated by Django 3.1 on 2020-10-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0004_auto_20201022_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order_item_order_number',
            field=models.IntegerField(verbose_name='Номер заказа'),
        ),
    ]

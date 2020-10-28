# Generated by Django 3.1 on 2020-09-15 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0028_auto_20200915_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Сумма'),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_item_quantity', models.PositiveIntegerField(default=1)),
                ('order_item_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='new_order.item')),
                ('order_item_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Товары', to='new_order.order', verbose_name='Номер заказа')),
            ],
        ),
    ]
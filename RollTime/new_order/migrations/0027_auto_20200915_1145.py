# Generated by Django 3.1 on 2020-09-15 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0026_auto_20200915_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_api',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='API'),
        ),
    ]

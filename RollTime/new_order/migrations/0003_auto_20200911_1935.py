# Generated by Django 3.1 on 2020-09-11 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_order', '0002_items_item_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
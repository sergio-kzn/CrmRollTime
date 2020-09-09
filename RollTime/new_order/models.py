from django.db import models


class Orders(models.Model):
    order_id = models.IntegerField(verbose_name="Номер заказа", unique=True)
    order_branch = models.CharField(verbose_name='Филиал', max_length=100)
    order_client = models.CharField(verbose_name='Клиент', max_length=100)
    order_courier = models.CharField(verbose_name='Курьер', max_length=100)
    order_items = models.JSONField(verbose_name='Товары')
    order_comment = models.TextField(verbose_name='Комментарий')
    order_date_time = models.DateTimeField(verbose_name='Время')
    order_payment = models.CharField(verbose_name='Оплата', max_length=100)
    order_status = models.CharField(verbose_name='Статус', max_length=100)
    order_delivery_address = models.CharField(verbose_name='Адрес доставки', max_length=100)
    order_history = models.JSONField(verbose_name='История')
    order_price = models.IntegerFieldField(verbose_name='Сумма')
    order_sale = models.JSONField(verbose_name='Скидка')
    order_marks = models.JSONField(verbose_name='Отметки')

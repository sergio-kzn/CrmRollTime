from django.db import models


class Category(models.Model):
    def __str__(self):
        return self.category_name

    category_id = models.AutoField(verbose_name='Номер категории', primary_key=True)
    category_name = models.CharField(verbose_name='Категория', max_length=100)
    category_show = models.BooleanField('Видимость', default=True)


class Color(models.Model):
    def __str__(self):
        return self.color

    color = models.CharField(verbose_name='Цвет', max_length=50)


class Item(models.Model):
    def __str__(self):
        return self.item_name

    item_id = models.AutoField(verbose_name='Номер товара', primary_key=True)
    item_index = models.IntegerField(verbose_name='Артикул', blank=True, null=True)
    item_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    item_name = models.CharField(verbose_name='Наименование', max_length=100, default='')
    item_price = models.IntegerField(verbose_name='Цена')
    item_color = models.ForeignKey(Color, on_delete=models.SET_NULL, blank=True, null=True)
    item_description = models.TextField(verbose_name='Описание', blank=True)
    item_show = models.BooleanField('Видимость', default=True)


class CurrentOrder(models.Model):
    # вкладка Заказ
    current_order_items = models.JSONField(verbose_name='Товары')
    # вкладка Детали
    current_order_branch = models.CharField(verbose_name='Филиал', max_length=100)
    current_order_client_phone = models.CharField(verbose_name='Телефон Клиента', max_length=100)
    current_order_client_name = models.CharField(verbose_name='Имя Клиента', max_length=100)
    current_order_delivery_address = models.CharField(verbose_name='Адрес доставки', max_length=100)
    current_order_comment = models.TextField(verbose_name='Комментарий')
    # вкладка Отметки
    current_order_date_time = models.DateTimeField(verbose_name='Время')
    current_order_certificate = models.CharField(verbose_name='Сертификат', max_length=100)
    current_order_learning_from = models.CharField(verbose_name='Узнали из', max_length=100)
    current_order_payment = models.CharField(verbose_name='Оплата', max_length=100)
    current_order_marks = models.JSONField(verbose_name='Отметки')
    # Подвал
    current_order_person = models.IntegerField('Приборы')
    current_order_sale = models.JSONField(verbose_name='Скидка')


class Order(models.Model):
    def __str__(self):
        return f'{self.order_id} {self.order_date_time}'
    # вкладка Заказ
    order_items = models.JSONField(verbose_name='Товары')
    # вкладка Детали
    order_branch = models.CharField(verbose_name='Филиал', max_length=100)
    order_client_phone = models.CharField(verbose_name='Телефон Клиента', max_length=100)
    order_client_name = models.CharField(verbose_name='Имя Клиента', max_length=100)
    order_delivery_address = models.CharField(verbose_name='Адрес доставки', max_length=100)
    order_comment = models.TextField(verbose_name='Комментарий')
    # вкладка Отметки
    order_date_time = models.DateTimeField(verbose_name='Время')
    order_certificate = models.CharField(verbose_name='Сертификат', max_length=100)
    order_learning_from = models.CharField(verbose_name='Узнали из', max_length=100)
    order_payment = models.CharField(verbose_name='Оплата', max_length=100)
    order_marks = models.JSONField(verbose_name='Отметки')
    # Подвал
    order_person = models.IntegerField('Приборы')
    order_sale = models.JSONField(verbose_name='Скидка')
    order_price = models.IntegerField(verbose_name='Сумма')
    # на странице Заказы
    order_id = models.IntegerField(verbose_name="Номер заказа", unique=True)
    order_status = models.CharField(verbose_name='Статус', max_length=100)
    order_courier = models.CharField(verbose_name='Курьер', max_length=100)
    order_history = models.JSONField(verbose_name='История')

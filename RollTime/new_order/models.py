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


class Order(models.Model):
    def __str__(self):
        return f'{self.order_id} {self.order_date_time}'
    order_id = models.AutoField(primary_key=True)
    # вкладка Заказ
    order_items = models.JSONField(verbose_name='Товары', blank=True, null=True)
    # вкладка Детали
    order_branch = models.CharField(verbose_name='Филиал', max_length=100, blank=True)
    order_client_phone = models.CharField(verbose_name='Телефон Клиента', max_length=15, blank=True)
    order_client_name = models.CharField(verbose_name='Имя Клиента', max_length=100, blank=True)
    order_delivery_street = models.CharField(verbose_name='Улица', max_length=100, blank=True, null=True)
    order_delivery_house = models.CharField(verbose_name='Дом', max_length=10, blank=True, null=True)
    order_delivery_entrance = models.CharField(verbose_name='Подъезд', max_length=10, blank=True, null=True)
    order_delivery_floor = models.CharField(verbose_name='Этаж', max_length=10, blank=True, null=True)
    order_delivery_flat = models.CharField(verbose_name='Квартира', max_length=10, blank=True, null=True)
    order_comment = models.TextField(verbose_name='Комментарий', blank=True)
    # вкладка Отметки
    order_date_time = models.DateTimeField(verbose_name='Время')
    order_certificate = models.CharField(verbose_name='Сертификат', max_length=100, blank=True)
    order_learning_from = models.CharField(verbose_name='Узнали из', max_length=100, blank=True)
    order_payment = models.CharField(verbose_name='Оплата', max_length=100)
    order_marks = models.JSONField(verbose_name='Отметки')
    # Подвал
    order_person = models.IntegerField('Приборы', default=1)
    order_sale = models.IntegerField(verbose_name='Скидка', default=0)
    order_price = models.IntegerField(verbose_name='Сумма', default=0)
    # на странице Заказы
    order_number = models.IntegerField(verbose_name="Номер заказа", default=0)
    order_status = models.CharField(verbose_name='Статус', max_length=100, blank=True)
    order_courier = models.CharField(verbose_name='Курьер', max_length=100, blank=True)
    order_history = models.JSONField(verbose_name='История', blank=True, null=True)

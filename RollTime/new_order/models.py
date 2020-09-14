from django.db import models


class LearningFrom(models.Model):
    """список источников, откуда приходят клиенты"""
    class Meta:
        verbose_name = "Узнали из"
        verbose_name_plural = "Узнали из"

    def __str__(self):
        return f'{self.learning_from_name}'

    learning_from_name = models.CharField(verbose_name='Название', max_length=100, blank=True)


class Branch(models.Model):
    """список филиалов"""
    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"

    def __str__(self):
        return f'{self.branch_name} - {self.branch_address}'

    branch_name = models.CharField(verbose_name='Название филиала', max_length=100, blank=True)
    branch_address = models.CharField(verbose_name='Адрес филиала', max_length=100, blank=True)
    branch_default = models.BooleanField(verbose_name='По умолчанию', default=False)


class Category(models.Model):
    """список категорий товаров, показывается на странице нового заказа в виде вкладок"""
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['category_sort']

    def __str__(self):
        return self.category_name

    category_id = models.AutoField(verbose_name='Номер категории', primary_key=True)
    category_name = models.CharField(verbose_name='Категория', max_length=100)
    category_show = models.BooleanField('Видимость', default=True)
    category_sort = models.IntegerField('Порядок', default=0)


class Color(models.Model):
    """цвет товара нужен для выделения. удобно когда товаров становится много"""
    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"

    def __str__(self):
        return self.color

    color = models.CharField(verbose_name='Цвет', max_length=50)


class Item(models.Model):
    """список товаров. связан с моделями Color и Category"""
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return f'{self.item_name} - {self.item_price}р.'

    item_id = models.AutoField(verbose_name='Номер товара', primary_key=True)
    item_index = models.IntegerField(verbose_name='Артикул', blank=True, null=True)
    item_category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE, blank=False)
    item_name = models.CharField(verbose_name='Наименование', max_length=100, default='')
    item_price = models.IntegerField(verbose_name='Цена')
    item_color = models.ForeignKey(Color, verbose_name='Цвет', on_delete=models.SET_NULL, blank=True, null=True)
    item_description = models.TextField(verbose_name='Описание', blank=True)
    item_show = models.BooleanField('Видимость', default=True)


class Order(models.Model):
    """
    список заказов.
    связан с формой на странице Новый заказ
    заказы можно посмотреть на странице Заказы
    """
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

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
    order_date_time = models.DateTimeField(verbose_name='Дата и время заказа', blank=True, null=True)
    order_certificate = models.CharField(verbose_name='Сертификат', max_length=100, blank=True)
    order_learning_from = models.CharField(verbose_name='Узнали из', max_length=100, blank=True)
    order_payment = models.CharField(verbose_name='Оплата', max_length=100, blank=True)
    order_marks = models.JSONField(verbose_name='Отметки', blank=True)
    # Подвал
    order_person = models.IntegerField('Приборы', blank=True)
    order_sale = models.IntegerField(verbose_name='Скидка', blank=True)
    order_price = models.IntegerField(verbose_name='Сумма', blank=True)
    # на странице Заказы
    order_number = models.IntegerField(verbose_name="Номер заказа", blank=True)
    order_status = models.CharField(verbose_name='Статус', max_length=100, blank=True)
    order_courier = models.CharField(verbose_name='Курьер', max_length=100, blank=True)
    order_history = models.JSONField(verbose_name='История', blank=True, null=True)

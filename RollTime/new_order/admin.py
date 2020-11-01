from django.contrib import admin

from .models import *


class ItemsInstanceInline(admin.TabularInline):
    """настройка отображения раздела Категории (список товаров)"""
    model = Item
    fields = ['item_index', 'item_name', 'item_price', 'item_color', 'item_show']
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    """настройка отображения раздела Категории"""
    list_display = ['category_name', 'category_show', 'count', 'category_sort']
    list_editable = ['category_sort']
    fields = ['category_id', 'category_name', 'category_show', 'category_sort']
    readonly_fields = ['category_id', 'count']
    inlines = [ItemsInstanceInline]

    def count(self, obj):
        return Item.objects.filter(item_category=obj).count()

    count.short_description = 'Кол-во'



class OrderItemsInline(admin.TabularInline):
    """Настройка отображения раздела Заказы (список товаров)"""
    # model = OrderItem
    # extra = 0
    pass


class OrderAdmin(admin.ModelAdmin):
    """Настройка отображения раздела Заказы"""
    list_display = ['order_number', 'order_status', 'order_date_time', 'order_price']
    # inlines = [OrderItemsInline]


class SaleAdmin(admin.ModelAdmin):
    list_display = ['sale', 'sale_order']
    list_editable = ['sale_order']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment_name', 'payment_api', 'payment_sort']
    list_editable = ['payment_api', 'payment_sort']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(Color)
admin.site.register(Branch)
admin.site.register(LearningFrom)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Payment, PaymentAdmin)

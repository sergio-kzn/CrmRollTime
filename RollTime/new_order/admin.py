from django.contrib import admin

from .models import *


class ItemsInstanceInline(admin.TabularInline):
    """настройка отображения раздела Категории (список товаров)"""
    model = Item
    fields = ['item_index', 'item_name', 'item_price', 'item_color', 'item_show']
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    """настройка отображения раздела Категории"""
    readonly_fields = ['category_id']
    fields = ['category_id', 'category_name', 'category_show', 'category_sort']
    list_display = ['category_name', 'category_show', 'category_sort']
    inlines = [ItemsInstanceInline]


class OrderItemsInline(admin.TabularInline):
    """Настройка отображения раздела Заказы (список товаров)"""
    # model = OrderItem
    # extra = 0
    pass

class OrderAdmin(admin.ModelAdmin):
    """Настройка отображения раздела Заказы"""
    list_display = ['order_number', 'order_status', 'order_date_time', 'order_price']
    # inlines = [OrderItemsInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(Color)
admin.site.register(Branch)
admin.site.register(LearningFrom)
admin.site.register(Sale)

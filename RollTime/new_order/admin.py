from django.contrib import admin

from .models import *


class ItemsInstanceInline(admin.TabularInline):
    """внешний вид для списка Товаров при редактировании Категории"""
    model = Item
    fields = ['item_index', 'item_name', 'item_price', 'item_color', 'item_show']
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['category_id']
    fields = ['category_id', 'category_name', 'category_show', 'category_sort']
    list_display = ['category_name', 'category_show', 'category_sort']
    inlines = [ItemsInstanceInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Color)
admin.site.register(Branch)
admin.site.register(LearningFrom)

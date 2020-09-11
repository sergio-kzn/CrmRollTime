from django.contrib import admin

from .models import Item, Order, Category


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['category_id']
    fields = ['category_id', 'category_name', 'category_show']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item)
admin.site.register(Order)

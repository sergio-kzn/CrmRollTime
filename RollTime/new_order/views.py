from django.shortcuts import render
from .models import *


def new_order(request):
    category_list = Category.objects.all()
    item_list = Item.objects.all()
    context = {'category_list': category_list,
               'item_list': item_list}
    print(context)

    if request.method == 'POST':
        print("!!!!!!!!!!!!!!!!!")

    return render(request, 'new_order/new_order.html', context)


def add_order_in_db(request):
    return render(request, 'new_order/new_order.html')

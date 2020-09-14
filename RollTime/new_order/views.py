from django.shortcuts import render
from .models import *
from .forms import *

from .services import add_order_in_db


def new_order(request):
    category_list = Category.objects.all()
    item_list = Item.objects.all()

    if request.method == 'POST':
        print('post')
        form = NewOrderForm(request.POST, auto_id=False)
        if form.is_valid():
            add_order_in_db(form.cleaned_data)
            print('valid')
        else:
            print('not valid')
            print('clean:', form.cleaned_data)
            print('post:', request.POST)
    else:
        print('get')
        form = NewOrderForm(auto_id=False)

    context = {'category_list': category_list,
               'item_list': item_list,
               'form': form}

    return render(request, 'new_order/new_order.html', context)

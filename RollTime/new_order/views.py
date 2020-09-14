from django.shortcuts import render
from .forms import *

from .services import add_order_in_db, prepare_context_for_html


def new_order(request):
    """страница создания нового заказа"""
    if request.method == 'POST':
        form = NewOrderForm(request.POST, auto_id=False)
        if form.is_valid():
            add_order_in_db(request.POST)
    else:
        form = NewOrderForm(auto_id=False)

    return render(request, 'new_order/new_order.html', prepare_context_for_html(form))

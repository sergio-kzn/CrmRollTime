from django.shortcuts import render
from .forms import *

from .services import prepare_context_for_html


def new_order(request):
    """страница создания нового заказа"""
    item_formset = modelformset_factory(OrderItem, form=ItemForm, extra=0)

    if request.method == 'POST':
        form = NewOrderForm(request.POST, auto_id=False)
        if form.is_valid():
            form.save()
        formset = item_formset(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        form = NewOrderForm(auto_id=False)
        formset = item_formset()

    return render(request, 'new_order/new_order.html', prepare_context_for_html(form, formset))

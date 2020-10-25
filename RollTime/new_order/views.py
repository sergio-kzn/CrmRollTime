from django.shortcuts import render, redirect
from .forms import NewOrderForm, ItemForm, modelformset_factory
from .models import OrderItem

from .services import prepare_context_for_html, create_new_order, create_new_order_number, payment_default


def new_order(request):
    """страница создания нового заказа"""
    item_formset = modelformset_factory(OrderItem, form=ItemForm, extra=0, can_delete=True)

    if request.method == 'POST':
        form = NewOrderForm(request.POST, auto_id=False)
        formset = item_formset(request.POST)
        if create_new_order(form, formset):
            return redirect('new_order:new_order_url')

    else:
        form = NewOrderForm(auto_id=False, initial={
            'order_branch': 1,
            'order_number': create_new_order_number(),
            'order_payment': payment_default(),
            'order_marks': 1,
        })
        formset = item_formset(queryset=OrderItem.objects.none())

    return render(request, 'new_order/new_order.html', prepare_context_for_html(form, formset))

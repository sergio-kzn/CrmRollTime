from django.shortcuts import render, redirect
from .forms import NewOrderForm, ItemForm, modelformset_factory
from .models import OrderItem, Order
from loguru import logger

from .services import prepare_context_for_html, create_new_order


def new_order(request):
    """страница создания нового заказа"""
    item_formset = modelformset_factory(OrderItem, form=ItemForm, extra=0, can_delete=True)

    if request.method == 'POST':
        form = NewOrderForm(request.POST, auto_id=False)
        formset = item_formset(request.POST)

        if form.is_valid():
            logger.success("form is valid")
            form.save()

            for f in formset:
                f.order_item_order_number = form.cleaned_data['order_number']
            logger.info("order_number changed")

            if formset.is_valid():
                logger.success("formset is valid")
                formset.save()
                create_new_order(form, formset)

                return redirect('new_order:new_order_url')

        if not form.is_valid():
            logger.error("FORM NO VALID")
        if not formset.is_valid():
            logger.error("FORMSET NO VALID")
            logger.debug(formset.errors)

    else:
        order_numbers = Order.objects.all().only('order_number')
        new_order_number = 0


        for order_number in order_numbers:
            if order_number.order_number > new_order_number:
                 new_order_number = order_number.order_number
        new_order_number += 1

        form = NewOrderForm(auto_id=False, initial={'order_number': new_order_number})
        formset = item_formset(queryset=OrderItem.objects.none())

    return render(request, 'new_order/new_order.html', prepare_context_for_html(form, formset))

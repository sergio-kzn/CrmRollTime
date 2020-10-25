from django.shortcuts import render, redirect
from .forms import NewOrderForm, ItemForm, modelformset_factory
from .models import OrderItem, Order

from .services import prepare_context_for_html, create_or_edit_order, create_new_order_number, payment_default


def new_order(request):
    """страница создания нового заказа"""

    item_formset = modelformset_factory(OrderItem, form=ItemForm, extra=0, can_delete=True)

    if request.method == 'POST':
        form = NewOrderForm(request.POST, auto_id=False)
        formset = item_formset(request.POST)
        if create_or_edit_order(form, formset):
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


def edit_order(request, order_id):
    """страница редактирования заказа"""

    item_formset = modelformset_factory(OrderItem, form=ItemForm, extra=0, can_delete=True)

    if request.method == 'POST':
        form = NewOrderForm(request.POST, auto_id=False)
        formset = item_formset(request.POST)
        if create_or_edit_order(form, formset, order_id):
            return redirect('orders_list:orders_list')
    else:
        # заполняем формы данными из таблицы.
        order_number = Order.objects.get(id=order_id).order_number
        formset_data = OrderItem.objects.filter(order_item_order_number=order_number)
        formset = item_formset(queryset=formset_data)

        # сделано через жопу, но работает стабильно.
        # сначала получает тип QuerySet
        # потом преобразуем его в list
        # переделать бы на objects.get(), но все равно будет через жопу
        form_data = Order.objects.filter(id=order_id)
        list_form_data = list(form_data.values())
        form = NewOrderForm(auto_id=False, initial=list_form_data[0])

    return render(request, 'new_order/new_order.html', prepare_context_for_html(form, formset))

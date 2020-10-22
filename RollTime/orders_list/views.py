from django.shortcuts import render

from new_order.models import Order, OrderItem


def orders_list(request):
    orders = Order.objects.all().order_by('-order_date_time', '-order_number')
    order_items = OrderItem.objects.all()
    context = {
        'orders': orders,
        'order_items': order_items,
    }
    return render(request, 'orders_list/orders_list.html', context)

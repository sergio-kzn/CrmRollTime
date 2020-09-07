from django.shortcuts import render


def new_order(request):
    return render(request, 'new_order/new_order.html')

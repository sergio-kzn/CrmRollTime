from django.shortcuts import render

def orders_list(request):
    return render(request, 'orders_list/orders_list.html')


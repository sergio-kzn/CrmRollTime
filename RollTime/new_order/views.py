from django.shortcuts import render


def new_order(request):

    return render(request, 'new_order/new_order.html')


def add_order_in_db(request):
    if request.method == 'POST':
        print("!!!!!!!!!!!!!!!!!")
    return render(request, 'new_order/new_order.html')

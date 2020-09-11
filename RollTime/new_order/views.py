from django.shortcuts import render
from .models import Category


def new_order(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    print(context)
    return render(request, 'new_order/new_order.html', context)


def add_order_in_db(request):
    if request.method == 'POST':
        print("!!!!!!!!!!!!!!!!!")

    return render(request, 'new_order/new_order.html')

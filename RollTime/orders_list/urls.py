from django.urls import path

from . import views


app_name = 'orders_list'
urlpatterns = [
    path('', views.orders_list, name='orders_list'),
]
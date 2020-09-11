from django.urls import path

from . import views


app_name = 'new_order'
urlpatterns = [
    path('', views.new_order, name='new_order'),
    path('add_order_in_db', views.add_order_in_db, name='add_order_in_db'),
]
from django.urls import path

from . import views


app_name = 'new_order'
urlpatterns = [
    path('', views.new_order, name='new_order'),
]
from django.urls import path

from . import views
# from .views import ItemUpdate

app_name = 'new_order'
urlpatterns = [
    path('<int:order_id>/', views.edit_order, name='edit_order_url'),
    # path('<pk>/', ItemUpdate.as_view(), name='edit_order_url'),
    path('', views.new_order, name='new_order_url'),
]

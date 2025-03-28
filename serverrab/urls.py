# myapp/urls.py
from django.urls import path
from .views import client_orders,worker_login, worker_orders
from .views import custom_login
from .views import update_price,search_client


urlpatterns = [
    path('client_orders/', client_orders, name='client_orders'),
    path('client_login/', custom_login, name='client_login'),
    path('worker_login/', worker_login, name='worker_login'),
    path('worker_orders/', worker_orders, name='worker_orders'),
    path('update_price/', update_price, name='update_price'),
    path('search_result/', search_client, name='search_client'),

    # Другие URL-шаблоны вашего приложения
]



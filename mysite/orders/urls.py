from django.urls import path
from . import views
urlpatterns=[
    path('add_address',views.add_address, name="add_address"),
    path('checkout', views.checkout, name = "checkout"),
    path('place_order', views.place_order, name = "place_order"),
    path('order_success', views.order_success, name="order_success"),
    path('order_failed', views.order_failed, name= "order_failed"),
]
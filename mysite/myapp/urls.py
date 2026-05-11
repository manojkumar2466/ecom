from django.urls import path
from . import views

app_name="myapp"

urlpatterns = [
    path('index/', views.index, name = "index"),
    path('detail/<slug:slug>',views.detail, name="detail"),
]

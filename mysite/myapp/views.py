from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        "products" : products
    }
    return render(request,"myapp/index.html", context)
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .cart import Cart
from myapp.models import Product
from  django.shortcuts import get_object_or_404
# Create your views here.
def cart_add(request):

    print("add cart view function called")
    cart = Cart(request)
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product_quantity = request.POST.get("product_quantity")
        product = get_object_or_404(Product, id=product_id)
        print(f"product added to cart with id: {product_id} and quantity: {product_quantity}")
        cart.add(product = product, product_quantity = product_quantity)
        cart_len = cart.__len__()
    return JsonResponse(
            {"cart_len":cart_len},
        )


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get("action")=="post":
        product_id = request.POST.get("product_id")
        cart.delete(product_id)
        cart_quantity = cart.__len__()
        cart_total = cart.get_total_price()
        return JsonResponse(
            {"cart_quantity":cart_quantity,
             "cart_total":cart_total,}
            )

def cart_update(request):
    cart= Cart(request)
    if request.POST.get("action")=="post":
        product_id =request.POST.get("product_id")
        product_quantity=request.POST.get("product_quantity")
        cart.update(product_id,product_quantity)
        return JsonResponse({"message":"product updated"})

        

def cart_overview(request):
    cart = Cart(request)
    context= {
        "cart" :cart
    }
    return render(request,"cart/cart_overview.html", context)
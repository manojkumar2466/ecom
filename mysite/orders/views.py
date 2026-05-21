from django.shortcuts import render, redirect
from .forms import AddressForm
from .models import Address
from cart.cart import Cart
from orders.models import Order, OrderItem
from django.http import JsonResponse

# Create your views here.
def add_address(request):

    try:
        address= Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        address =None

   
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return redirect('myapp:index')
    form = AddressForm(instance= address)
    context = {
        'form' :form,
    }
    return render(request,'orders/add_address.html', context )


def checkout(request):

    if request.user.is_authenticated:
        try:
            address = Address.objects.get(user = request.user)
            context ={
                "address" : address,
            }
            return render(request,"orders/checkout.html",context)
        except:
            return render(request, "orders/checkout.html")   
    return render(request, "orders/checkout.html")

def place_order(request):
    
    order_complete = False
    if request.method == "POST":

        cart = Cart(request)
        total_price = cart.get_total_price()

        user = request.user if request.user.is_authenticated else None

        order = Order.objects.create(user= user, total_amount = total_price)

        for item in cart:
            OrderItem.objects.create(order = order, product = item["product"],quantity = item["quantity"])
        order_complete = True
    return JsonResponse({"message":order_complete,})


def order_success(request):
    return render(request, "orders/order_success.html")

def order_failed(request):
    return render(request, "ordes/order_failed.html")
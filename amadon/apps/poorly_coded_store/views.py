from django.shortcuts import render, redirect, reverse
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process(request):
    product_id = request.POST["product_id"]
    quantity = int(request.POST["quantity"])
    price = float(Product.objects.get(id=product_id).price)
    total_price = "{0:.2f}".format(quantity * price)

    order = Order.objects.create(quantity_ordered=quantity, total_price=total_price)
    print("order placed")
    return redirect(reverse('checkout', kwargs={'id':order.id}))

def checkout(request, id):
    order = Order.objects.get(id=id)

    return render(request, "store/checkout.html", {'order': order})
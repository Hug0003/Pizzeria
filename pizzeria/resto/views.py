from django.shortcuts import render, get_object_or_404, redirect
from resto.models import Product, Cart, Order
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "resto/detail.html", context={"product": product})

def index(request):
    products =Product.objects.all()
    return render(request, 'resto/index.html', context={"products": products})

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)
    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse("product", kwargs={"slug":slug}))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'resto/cart.html', context={"orders":cart.orders.all()})


def delete_cart(request):
    cart = request.user.cart
    if cart:
        cart.delete()
    
    return redirect('index')


def api_get_plats(request):
    products = Product.objects.all()
    json = serializers.serialize("json", products)
    return HttpResponse(json)





def alcool(request):
    products =Product.objects.all()
    return render(request, 'resto/alcool.html', context={"products": products})

def cafe(request):
    products =Product.objects.all()
    return render(request, 'resto/cafe.html', context={"products": products})

def charcuterie(request):
    products =Product.objects.all()
    return render(request, 'resto/charcuterie.html', context={"products": products})

def d_sale(request):
    products =Product.objects.all()
    return render(request, 'resto/d_sale.html', context={"products": products})

def d_sucre(request):
    products =Product.objects.all()
    return render(request, 'resto/d_sucre.html', context={"products": products})

def lasagne(request):
    products =Product.objects.all()
    return render(request, 'resto/lasagne.html', context={"products": products})

def non_alcool(request):
    products =Product.objects.all()
    return render(request, 'resto/non_alcool.html', context={"products": products})

def pate(request):
    products =Product.objects.all()
    return render(request, 'resto/pate.html', context={"products": products})

def pizza(request):
    products =Product.objects.all()
    return render(request, 'resto/pizza.html', context={"products": products})

def salade(request):
    products =Product.objects.all()
    return render(request, 'resto/salade.html', context={"products": products})

def sale(request):
    products =Product.objects.all()
    return render(request, 'resto/sale.html', context={"products": products})

def soda(request):
    products =Product.objects.all()
    return render(request, 'resto/soda.html', context={"products": products})

def sucre(request):
    products =Product.objects.all()
    return render(request, 'resto/sucre.html', context={"products": products})

def the(request):
    products =Product.objects.all()
    return render(request, 'resto/the.html', context={"products": products})
from django.shortcuts import render
from .models import Product

def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html',{'products':products})
def order(request):
    return render(request,'shop/orsers.html')
def creative_order(request):
    return render(request,'shop/creative_order.html')
def product_detail(request):
    return render(request,'shop/product_detail.html')


from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    order = Order.objects.all()
    customer = Customer.objects.all()

    context = {'orders' : order, 'customers': customer}

    return render(request, 'accounts/dashboard.html', context)
    
def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products': products})

def customer(request):
    return render(request, 'accounts/customer.html')  

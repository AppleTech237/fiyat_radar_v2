

from django.shortcuts import render
from products.models import Product 

def home(request):
    items = Product.objects.all() 
    return render(request, 'pages/home.html', {'products': items})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

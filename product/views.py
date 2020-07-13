from django.shortcuts import render 
from product.models import *

# Create your views here.
def products(request):
    context = {}
    context["products"] =  Product.objects.filter(aviable=True)
    return render(request , "product/products.html", context)
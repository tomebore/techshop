from django.shortcuts import render , HttpResponse

# Create your views here.
def products(request):
    return HttpResponse(" <h1> список товаров </h1>")
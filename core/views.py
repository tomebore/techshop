from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
def home(request):
    return redirect("products")

def test(request):
    return HttpResponse("testpage")
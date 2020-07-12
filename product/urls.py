from django.conf.urls import include
from django.urls import path
from .views import products

urlpatterns = [
    path("", products , name="products"),
]
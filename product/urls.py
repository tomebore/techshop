from django.conf.urls import include
from django.urls import path
from .views import products

urlpatterns = [
    path("all/", products , name="products"),
]
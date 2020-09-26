from django.conf.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path("all/", products , name="products"),
    path("<int:id>/", product , name="product"),
    path("create/",product_create, name="product-create"),
]
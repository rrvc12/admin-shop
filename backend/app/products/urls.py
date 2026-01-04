from django.urls import path
from . import api


urlpatterns = [
    path("products-home/", api.ProductHomeAPI.as_view(), name="product-home"),
    path("products-list/", api.ProductListAPI.as_view(), name="product-list"),
]

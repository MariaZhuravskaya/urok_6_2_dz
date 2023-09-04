from django.urls import path
from catalog.views import index, contact, products, product, catalog_products, underwear, outerwear

urlpatterns = [
    path('', index),
    path('contacts', contact),
    path('products', products),
    path('catalog_products', catalog_products),
    path('catalog_products/underwear', underwear),
    path('catalog_products/outerwear', outerwear),
    path('catalog_products/underwear/<int:product_id>', product),
    path('catalog_products/outerwear/<int:product_id>', product),
]
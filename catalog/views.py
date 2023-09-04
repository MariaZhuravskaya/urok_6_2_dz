import json

from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Product, Contact, Category


def index(request):
    if request.method == 'GET':
        list_product = Product.objects.all()
        return render(request, 'catalog/index.html', {'products': list_product})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name}, {phone},{message}")
    list_contact = Contact.objects.all()
    return render(request, 'catalog/contact.html', {'contacts': list_contact})


def products(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        image = request.POST.get('image')
        categoria = request.POST.get('categoria')
        price = request.POST.get('price')
        date_creation = request.POST.get('date_creation')
        date_change = request.POST.get('date_change')
        print(f"{name}, {description},{image}, {categoria}, {price}")
        list_product = Product.objects.all()
        return render(request, 'catalog/product.html', {'products': list_product})


def catalog_products(request):
    if request.method == 'GET':
        list_product = Category.objects.all()
        return render(request, 'catalog/catalog_products.html', {'catalog_products': list_product})


def underwear(request):
    if request.method == 'GET':
        # SELECT id, name FROM public.catalog_category where name = 'Нижнее белье'
        underwear_category = Category.objects.filter(name='Нижнее белье')
        # select * from catalog_product where categoria_id = 2
        list_product = Product.objects.filter(categoria=underwear_category[0])
        return render(request, 'catalog/underwear.html', {'underwear_products': list_product})


def outerwear(request):
    if request.method == 'GET':
        # SELECT id, name FROM public.catalog_category where name = 'Верхняя одежда'
        outerwear_category = Category.objects.filter(name='Верхняя одежда')
        # select * from catalog_product where categoria_id = 2
        list_product = Product.objects.filter(categoria=outerwear_category[0])
        return render(request, 'catalog/outerwear.html', {'outerwear_products': list_product})


def product(request, product_id):
    if request.method == 'GET':
        p = Product.objects.get(id=product_id)
        return render(request, 'catalog/product.html', {'product': p})

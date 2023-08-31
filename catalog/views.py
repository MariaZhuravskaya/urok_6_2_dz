import json

from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Product, Contact


def index(request):
    if request.method == 'GET':
        p = Product.objects.filter()
        print(p[:5])
    return render(request, 'catalog/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name}, {phone},{message}")
    list_contact = Contact.objects.all()
    return render(request, 'catalog/contact.html', {'contacts': list_contact})



# Create your views here.

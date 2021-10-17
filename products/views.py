# Загрузка динамического контента в контроллер products посредством обычного словаря осуществляется так же,
# как и с помощью json-файла, только словарь с данными задается напрямую в context['products']

from django.shortcuts import render
from datetime import datetime
from .models import ProductCategory, Product

# Create your views here.


def date():
    return datetime.today()


def index(request):
    context = {'title': 'GeekShop',
               'date': date()}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
        'date': date(),
        'year': datetime.now().year
    }
    return render(request, 'products/products.html', context)

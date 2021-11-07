# Загрузка динамического контента в контроллер products посредством обычного словаря осуществляется так же,
# как и с помощью json-файла, только словарь с данными задается напрямую в context['products']

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime
from .models import ProductCategory, Product

# Create your views here.


def index(request):
    context = {'title': 'GeekShop',
               'date': datetime.today()}
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    try:
       products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator)
    context = {
        'title': 'GeekShop - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
        'date': datetime.today(),
        'year': datetime.now().year
    }
    return render(request, 'products/products.html', context)

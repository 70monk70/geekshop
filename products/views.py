# Загрузка динамического контента в контроллер products посредством обычного словаря осуществляется так же,
# как и с помощью json-файла, только словарь с данными задается напрямую в context['products']

from django.shortcuts import render
from datetime import datetime
import json

# Create your views here.

with open('products/fixtures/products.json', encoding='UTF-8') as j:
    json_file = json.load(j)


def date():
    return datetime.today()


def index(request):
    context = {'title': 'GeekShop',
               'date': date()}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': json_file['products'],
        'categories': [
            'новинки',
            'одежда',
            'обувь',
            'аксессуары',
            'подарки'
        ],
        'date': date(),
        'year': datetime.now().year
    }
    return render(request, 'products/products.html', context)

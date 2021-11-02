from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from datetime import datetime


from products.models import Product, ProductCategory
from baskets.models import Basket

# Create your views here.


@login_required
def basket_add(request, product_id):

    if request.is_ajax():
        product = Product.objects.get(id=product_id)
        baskets = Basket.objects.filter(user=request.user, product=product)
        if not baskets.exists():
            Basket.objects.create(user=request.user, product=product, quantity=1)
            message = messages.success(request, 'Товар добавлен в корзину!')
        elif baskets.first().quantity < product.quantity:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        else:
            message = messages.error(request, 'Таких товаров больше нет!')
        context = {
            'title': 'GeekShop - Каталог',
            'products': Product.objects.all(),
            'categories': ProductCategory.objects.all(),
            'date': datetime.today(),
            'year': datetime.now().year,
            'user': request.user,
        }
        result = render_to_string('products/products.html', context)
        return JsonResponse({'result': result})


@login_required
def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    messages.success(request, 'Вы удалили товар из корзины!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_edit(request, id, quantity):
    if request.is_ajax():
        basket = Basket.objects.get(id=id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()
    baskets = Basket.objects.filter(user=request.user)
    context = {'baskets': baskets}
    result = render_to_string('baskets/baskets.html', context)
    return JsonResponse({'result': result})

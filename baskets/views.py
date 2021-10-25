from django.shortcuts import HttpResponseRedirect
from django.contrib import messages

from products.models import Product
from baskets.models import Basket

# Create your views here.


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    elif baskets.first().quantity < product.quantity:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        messages.success(request, 'Таких товаров больше нет!')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    messages.success(request, 'Вы удалили товар из корзины!')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

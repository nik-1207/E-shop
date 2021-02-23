from django.shortcuts import render
from django.views import View

from store.models.Product import Product


class Cart(View):
    def get(self, response):
        ids = list(response.session.get('cart').keys())
        products = Product.getProductbyId(ids)
        print(products)
        return render(response, 'cart.html', {'productList': products})
        pass

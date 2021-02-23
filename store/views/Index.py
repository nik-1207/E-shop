from django.shortcuts import render, redirect
from django.views import View

from store.models.Category import Category
from store.models.Product import Product


class Index(View):

    def get(self, response):
        customer_Products = None
        if response.session.get('cart') == None:
            response.session['cart'] = {}
        productList = Product.getAllProducts()
        categoryList = Category.getAllCategories()
        category_id = response.GET.get('category')
        if category_id:
            productList = Product.getSpecificProducts(category_id)
        return render(response, 'index.html ', {'productList': productList, 'categoryList': categoryList})

    def post(self, response):
        remove = response.POST.get('remove')
        product_id = response.POST.get('product_id')
        cart = response.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] -= 1
                else:
                    cart[product_id] += 1
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        response.session['cart'] = cart
        # todo:remove print after debugging
        print(response.session['cart'])
        return redirect('homepage')

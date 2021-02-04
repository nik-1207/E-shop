from django.shortcuts import render
from django.views import View

from store.models.Category import Category
from store.models.Product import Product


class Index(View):
    def get(self, response):
        productList = Product.getAllProducts()
        categoryList = Category.getAllCategories()
        category_id = response.GET.get('category')
        if category_id:
            productList = Product.getSpecificProducts(category_id)
        return render(response, 'index.html', {'productList': productList, 'categoryList': categoryList})

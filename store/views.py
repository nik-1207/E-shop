from django.shortcuts import render

from .models.Category import Category
# Create your views here.
from .models.Product import Product


def index(response):
    productList = Product.getAllProducts()
    categoryList = Category.getAllCategories()
    return render(response, 'index.html', {'productList': productList, 'categoryList': categoryList})

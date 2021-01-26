from django.shortcuts import render

from .models.Category import Category
from .models.Customer import Customer
from .models.Product import Product


def index(response):
    productList = Product.getAllProducts()
    categoryList = Category.getAllCategories()
    category_id = response.GET.get('category')
    if category_id:
        productList = Product.getSpecificProducts(category_id)
    return render(response, 'index.html', {'productList': productList, 'categoryList': categoryList})


def signup(response):
    if response.method == 'GET':
        return render(response, 'signup.html')
    user_dict = response.POST
    print(response.POST)
    new_customer = Customer.objects.create(first_name=user_dict.get('fname'),
                                           last_name=user_dict.get('lname'),
                                           phone=user_dict.get('phone'),
                                           email=user_dict.get('email'),
                                           password=user_dict.get('pswd'))
    new_customer.save()
    return index(response)

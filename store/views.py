from django.contrib.auth.hashers import make_password
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
    new_customer = Customer(first_name=user_dict.get('fname'),
                            last_name=user_dict.get('lname'),
                            phone=user_dict.get('phone'),
                            email=user_dict.get('email'),
                            password=make_password(user_dict.get('pswd')))
    try:
        # check preexisting email
        Customer.objects.get(email=new_customer.email)
        # if email pre exist error is displayed on form
        return render(response, 'signup.html', {'error': 'Email already exist'})
        # email already exist
    except:
        new_customer.save()
        return index(response)


def login(response):
    if response == 'GET':
        return render(response, 'login.html')
    else:
        email = response.POST.get('email')
        password = response.POST.get('pswd')
        # Todo: adjust method to have proper functionality of signup
        '''try:
           cust_obj=Customer.objects.get(email=email)
            flag=check_password(cust_obj.password,password)
            print(flag)
            if flag:
                print('Login successfull')
                return index(response)
            return render(response, 'login.html', {'error': 'Incorrect Password'})
        except:
            return render(response, 'login.html',{'error':'account does not exist'})'''

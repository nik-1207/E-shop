from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View

from store.models.Customer import Customer


class Signup(View):
    def get(self, response):
        return render(response, 'signup.html')

        pass

    def post(self, response):
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
            return redirect('homepage')
        pass

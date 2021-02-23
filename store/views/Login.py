from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.views import View

from store.models.Customer import Customer


class Login(View):
    def get(self, response):
        return render(response, 'login.html')
        pass

    def post(self, response):
        email = response.POST.get('email')
        password = response.POST.get('pswd')
        try:

            existing_customer = Customer.objects.get(email=email)
            if check_password(password, existing_customer.password):
                response.session['customer_id'] = existing_customer.id
                response.session['customer_email'] = existing_customer.email
                return redirect('homepage')
            else:
                return render(response, 'login.html', {'error': 'wrong password!'})

        except:
            return render(response, 'login.html', {'error': 'user does not exist'})

        pass
def logout(response):
    response.session.clear()
    return redirect('login')

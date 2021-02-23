from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import Index, Signup, Login, Cart
from .views.Login import logout

urlpatterns = [
                  path('', Index.Index.as_view(), name='homepage'),
                  path('signup', Signup.Signup.as_view(), name='signup'),
                  path('login', Login.Login.as_view(), name='login'),
                  path('logout', logout, name='logout'),
                  path('cart', Cart.Cart.as_view(), name='cart')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index, signup, login

urlpatterns = [
                  path('', index),
                  path('signup', signup),
                  path('login', login)

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

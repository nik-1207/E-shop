from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index, signup

urlpatterns = [
                  path('', index),
                  path('signup', signup)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

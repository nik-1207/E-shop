from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import Index, Signup, Login

urlpatterns = [
                  path('', Index.as_view()),
                  path('signup', Signup.as_view()),
                  path('login', Login.as_view())

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

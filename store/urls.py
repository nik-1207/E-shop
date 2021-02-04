from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import Index, Signup, Login

urlpatterns = [
                  path('', Index.Index.as_view(), name='homepage'),
                  path('signup', Signup.Signup.as_view()),
                  path('login', Login.Login.as_view())

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

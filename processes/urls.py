from django.urls import path
from .views import contactForm
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
     path('getcontactform/', csrf_exempt(contactForm))
]

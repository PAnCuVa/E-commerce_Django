"""
URL configuration for sitioEcommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("users/login", views.login_view, name="login"),
    path("users/logout", views.logout_view, name="logout"),
    path('admin/', admin.site.urls),
    path('categories/', 
         include('products_and_services.urls')),
    path('productrating/',
         include('products_and_services.urls')),
    path('products/',
         include('products_and_services.urls')),
    path('contact/',
         include('processes.urls')),
    path('shoppingcart/',
         include('processes.urls')),
    path('workorders/',
         include('processes.urls')),
    path('promocodes/',
         include('processes.urls')),
    path('paymentmethods/',
         include('processes.urls')),
    path('purchaseorders/',
         include('processes.urls')),
    path('returns/',
         include('processes.urls')),
    # path('documentype/',
    #      include('users.urls')),
    # path('departments/',
    #      include('users.urls')),
    # path('Township/',
    #      include('users.urls')),
    # path('address/',
    #      include('users.urls'))
]

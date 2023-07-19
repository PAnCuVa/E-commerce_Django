from django.urls import path
from .views import categories, productRating, products

urlpatterns = [
     path('getcategories/', categories),
     path('getproductrating/', productRating),
     path('getproducts/', products)
]

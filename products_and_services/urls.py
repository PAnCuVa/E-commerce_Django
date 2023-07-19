from django.urls import path
from .views import categories, productRating, products
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
     path('getcategories/', csrf_exempt(categories)),
     path('getproductrating/', csrf_exempt(productRating)),
     path('getproducts/', csrf_exempt(products))
]

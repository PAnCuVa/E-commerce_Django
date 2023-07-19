from django.shortcuts import render
from .models import Categories, Product_Rating, Products
from .serializers import CategorieSerializer, ProductRatingSerializer, ProductSerializer
from django.http import JsonResponse


# Create your views here.
def categories(request):
    if request.method == 'GET':
        showAllCategories = Categories.objects.all()
        serializedCategories = CategorieSerializer(showAllCategories, many=True)
        return JsonResponse(serializedCategories.data, safe=False)
    

def productRating(request):
    if request.method == 'GET':
        showAllProductRating = Product_Rating.objects.all()
        serializedProductRating = ProductRatingSerializer(showAllProductRating, many=True)
        return JsonResponse(serializedProductRating.data, safe=False)
    

def products(request):
    if request.method == 'GET':
        showAllProducts = Products.objects.all()
        serializedProducts = ProductSerializer(showAllProducts, many=True)
        return JsonResponse(serializedProducts.data, safe=False)
    



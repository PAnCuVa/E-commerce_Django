from django.shortcuts import render
from .models import Categories, Product_Rating, Products
from .serializers import CategorieSerializer, ProductRatingSerializer, ProductSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser


# Create your views here.
def categories(request):
    if request.method == 'GET':
        showAllCategories = Categories.objects.all()
        serializedCategories = CategorieSerializer(showAllCategories, many=True)
        return JsonResponse(serializedCategories.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serialized = CategorieSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data, status = status.HTTP_200_OK)
        return JsonResponse(serialized.errors, status = status.HTTP_400_BAD_REQUEST)
    

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
    



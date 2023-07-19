from rest_framework import serializers
from .models import Categories, Product_Rating, Products


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('category_name', 'description')

class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Rating
        fields = ['value']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


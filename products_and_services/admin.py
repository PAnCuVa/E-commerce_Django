from django.contrib import admin
from .models import Categories, Product_Rating, Products

# Register your models here.
admin.site.register(Categories)
admin.site.register(Product_Rating)
admin.site.register(Products)



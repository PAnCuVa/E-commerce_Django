from django.db import models

# Create your models here.
class Categories (models.Model):
    category_name = models.CharField(max_length=30)
    category_status = models.CharField(max_length=10)
    description = models.TextField(max_length=200, null=True)
    
    def __str__(self):
        return f'{self.category_name}'
    

class Product_Rating (models.Model):
    value = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f'{self.value}'

  
class Products (models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=False, blank=False)
    product_name = models.CharField(max_length=30)
    stock = models.IntegerField()
    purchase_value = models.FloatField()
    sale_value = models.FloatField()
    product_rating = models.ForeignKey(Product_Rating, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.product_name}'


 
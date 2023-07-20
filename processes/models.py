from django.db import models

from products_and_services.models import Products
from users.models import Shipping_Address

# Create your models here.
class Contact_Form (models.Model):
    contact_name = models.CharField(max_length=50, blank=False, null=False)
    contact_phone_number = models.PositiveIntegerField(blank=False, null=False)
    contact_email = models.EmailField(blank=False, null=False)
    contact_message = models.TextField(max_length=300, blank=False, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'000{self.id} : {self.contact_name}'
    

class Shopping_Cart (models.Model):
    #doc_number
    product = models.ManyToManyField(Products, blank=True)
    quantity = models.PositiveIntegerField()
    total = models.FloatField()
    cart_creation_date = models.DateField(auto_now_add=True)
    cart_status = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id} : {self.cart_status}' 

    
class Work_Orders (models.Model):
    #doc number
    request_type = models.CharField(max_length=30, blank=False, null=False)
    device = models.CharField(max_length=30, blank=False, null=False)
    brand = models.CharField(max_length=20, blank=False, null=False)
    reference = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField(max_length=200)
    attachments =models.FileField(upload_to=None)
    cart_creation_date = models.DateField(auto_now_add=True)
    work_status = models.CharField(max_length=15)

    def __str__(self):
        return f'000{self.id} : {self.request_type} : {self.work_status}'
    

class Promo_Codes (models.Model):
    code = models.CharField(max_length=10)
    percentage = models.FloatField()
    code_status = models.CharField( max_length=15)

    def __str__(self):
        return f'{self.code}'


class Payment_Methods (models.Model):
    payment_method_name = models.CharField( max_length=30)

    def __str__(self):
        return f'{self.payment_method_name}'


class Purchase_Orders (models.Model):
    shopping_cart = models.OneToOneField(Shopping_Cart, on_delete=models.CASCADE, null=False, blank=False)
    payment_methods = models.ForeignKey(Payment_Methods, on_delete=models.CASCADE, null=False, blank=False)
    shipping_address = models.ForeignKey(Shipping_Address, on_delete=models.CASCADE, null=False, blank=False)
    promo_codes = models.ForeignKey(Promo_Codes, on_delete=models.CASCADE, null=True, blank=True)
    order_creation_date = models.DateField(auto_now_add=True)
    order_status = models.CharField(max_length=15)

    def __str__(self):
        return f'000{self.id} : {self.order_status}'
    

class Returns (models.Model):
    #doc number
    purchase_order = models.OneToOneField(Purchase_Orders, on_delete=models.CASCADE, null=False, blank=False)
    return_status = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.id} : {self.return_status_status}'
    




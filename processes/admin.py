from django.contrib import admin
from .models import Contact_Form, Shopping_Cart, Work_Orders, Promo_Codes, Payment_Methods, Purchase_Orders, Returns

# Register your models here.
admin.site.register(Contact_Form)
admin.site.register(Shopping_Cart)
admin.site.register(Work_Orders)
admin.site.register(Promo_Codes)
admin.site.register(Payment_Methods)
admin.site.register(Purchase_Orders)
admin.site.register(Returns)
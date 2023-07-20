from django.contrib import admin
from .models import Document_Type, Departments, Township, Shipping_Address

# Register your models here.
admin.site.register(Document_Type)
admin.site.register(Departments)
admin.site.register(Township)
admin.site.register(Shipping_Address)

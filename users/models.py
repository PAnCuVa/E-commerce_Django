from django.db import models

# Create your models here.
class Document_Type (models.Model):
    doc_type_name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return f'{self.doc_type_name}'
    

class Departments (models.Model):
    department_name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return f'{self.department_name}'
    

class Township (models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=False, blank=False)
    township_name = models.CharField(max_length=20, blank=False, null=False)
    postal_code = models.SmallIntegerField()

    def __str__(self):
        return f'{self.township_name}'
    

class Shipping_Address (models.Model):
    #doc number
    township = models.ForeignKey(Township, on_delete=models.CASCADE, null=False)
    neighborhood = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50, blank=False, null=False)
    references = models.CharField(max_length=50)
    default_address = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.address}'
    
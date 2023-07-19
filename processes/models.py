from django.db import models

# Create your models here.
class Contact_Form (models.Model):
    contact_name = models.CharField(max_length=50, blank=False, null=False)
    contact_phone_number = models.PositiveIntegerField(blank=False, null=False)
    contact_email = models.EmailField(blank=False, null=False)
    contact_message = models.TextField(max_length=300, blank=False, null=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'000{self.id} : {self.contact_name}'
from rest_framework import serializers
from .models import Contact_Form


class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_Form
        fields = ('contact_name', 'contact_phone_number', 'contact_email', 'contact_message')




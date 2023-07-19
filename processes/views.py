from django.shortcuts import render
from .models import Contact_Form
from .serializers import ContactFormSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser


# Create your views here.
def contactForm(request):
    if request.method == 'GET':
        showAllContactForm = Contact_Form.objects.all()
        serializedContactForm = ContactFormSerializer(showAllContactForm, many=True)
        return JsonResponse(serializedContactForm.data, safe=False)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serialized = ContactFormSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data, status = status.HTTP_200_OK)
        return JsonResponse(serialized.errors, status = status.HTTP_400_BAD_REQUEST)
    
    
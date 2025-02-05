from django.http import JsonResponse  # Add this import!
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer  # No circular import

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

def home_view(request):
    return JsonResponse({"message": "Welcome to the FAQ API!"})

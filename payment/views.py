from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializer import PaymentSerializer
from .models import PaymentStudent
class PaymentViewset(ModelViewSet):
    queryset = PaymentStudent.objects.all()
    serializer_class = PaymentSerializer
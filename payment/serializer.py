from rest_framework import serializers
from .models import PaymentStudent
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentStudent
        fields = '__all__'
from rest_framework import serializers
from .models import Student
from payment.serializer import PaymentSerializer
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name','paymentstudent','one_id','image','phone']
        depth =1
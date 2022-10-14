from rest_framework import serializers
from .models import ClassRoom
class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'
        depth =1
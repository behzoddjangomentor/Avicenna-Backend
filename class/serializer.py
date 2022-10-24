from rest_framework import serializers
from .models import ClassRoom,Davomat
class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = '__all__'
        depth =1
class DavomatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields= '__all__'
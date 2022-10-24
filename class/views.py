from django.shortcuts import render
# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import ClassRoom,Davomat
from .serializer import ClassRoomSerializer,DavomatSerializer
class ClassRoomViewset(ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
class GetClassRoomCount(APIView):
    def get(self,request):
        count = ClassRoom.objects.all().count()
        data = {
            'count': count
        }
        return Response(data=data,status=status.HTTP_200_OK)
class DavomatViewset(ModelViewSet):
    queryset = Davomat.objects.all()
    serializer_class = DavomatSerializer
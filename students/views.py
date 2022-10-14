from django.shortcuts import render

# Create your views here.
from .models import Student
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .serializer import StudentSerializer
class StudentInfoViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentInfo(APIView):
    def get(self,request,one_id):
        data = Student.objects.filter(one_id=one_id)
        serializer =StudentSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
class GetStudentCount(APIView):
    def get(self,request):
        count = Student.objects.all().count()
        data = {
            'count': count
        }
        return Response(data=data,status=status.HTTP_200_OK)

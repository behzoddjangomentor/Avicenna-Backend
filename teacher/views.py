from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import  Max
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import FanTest,BlokTestlar,Teacher
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404,get_list_or_404
from .serilizer import *
class FanTestView(APIView):
    def get(self,request,test_kodi,tel):
        result = FanTest.objects.filter(Q(test_kodi = test_kodi) & Q(tel=tel))
        serializer = FanTestSerializer(result,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)


class BlokTestlarView(APIView):
    def get(self, request,week_code):
        result = BlokTestlar.objects.filter(week_code=week_code).last()
        serializer = BlokTestlarSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)
class CheckIt(APIView):
    def get(self,request,test_kodi):
        if FanTest.objects.filter(test_kodi = test_kodi).exists():
            return Response({"status":"OK"},status=status.HTTP_200_OK)
        else:
            return Response({"status": "BAD"}, status=status.HTTP_204_NO_CONTENT)
# class CheckBlok(APIView):
#     def get(self,request,test_kodi):
#         if BlokTestlar.objects.filter(test_kodi = test_kodi).exists():
#             return Response({"status":"OK"},status=status.HTTP_200_OK)
#         else:
#             return Response({"status": "BAD"}, status=status.HTTP_204_NO_CONTENT)
import json
class TestResultImage(APIView):
    def get(self,request,global_id):
        current = list(BlokTestlar.objects.filter(global_id=global_id).values('ball'))
        datame= BlokTestlar.objects.filter(global_id=global_id).values('first_block','second_block')[0]
        get_max = BlokTestlar.objects.filter(first_block=datame['first_block'],second_block=datame['second_block'])
        maximums = list(get_max.order_by('-ball').values('ball')[:5])  
        return JsonResponse(data={"self":current,"max":maximums},safe=False)
        
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class GetTeacherCount(APIView):
    def get(self,request):
        count = Teacher.objects.all().count()
        data = {
            'count': count
        }
        return Response(data=data,status=status.HTTP_200_OK)

class LastTestResult(ModelViewSet):
    queryset = FanTest.objects.order_by('-id')[:1]
    serializer_class = FanTestSerializer
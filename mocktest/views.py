from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import BotUsers
from rest_framework.response import Response
from rest_framework.views import APIView
from  rest_framework import status
from .serializer import BotUsersSerializer
class BotUsersViewset(ModelViewSet):
    queryset = BotUsers.objects.all()
    serializer_class = BotUsersSerializer
class GetBotUserCount(APIView):
    def get(self,request):
        count = BotUsers.objects.all().count()
        data = {
            'count': count
        }
        return Response(data=data,status=status.HTTP_200_OK)

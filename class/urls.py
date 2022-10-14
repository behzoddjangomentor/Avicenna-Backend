from django.urls import path,include
from .views  import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('class',ClassRoomViewset)
urlpatterns = [
    path('',include(router.urls)),
    path('getclasscount/',GetClassRoomCount.as_view())
]
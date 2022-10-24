from rest_framework.routers import DefaultRouter
from .views import BotUsersViewset,GetBotUserCount
from teacher.views import FanTestView,BlokTestlarView,CheckIt,TestResultImage
from payment.views import PaymentViewset
from django.urls import path,include
from teacher.views import GetTeacherCount,FanTestAllView
from students.views import GetStudentCount,StudentInfo,StudentInfoViewset
router = DefaultRouter()
router.register('newuser',BotUsersViewset),
router.register('studentinfoviewset',StudentInfoViewset),
router.register('payment',PaymentViewset),

urlpatterns = [
    path('',include(router.urls)),
    path('fantest/<str:test_kodi>/<str:tel>/',FanTestView.as_view()),
    path('fantestall/<str:test_kodi>/',FanTestAllView.as_view()),
    path('bloktest/<str:week_code>/', BlokTestlarView.as_view()),
    path('checkfantest/<str:test_kodi>/', CheckIt.as_view()),
    path('getstudentcount/',GetStudentCount.as_view()),
    path('getbotusercount/',GetBotUserCount.as_view()),
    path('getteachercount/',GetTeacherCount.as_view()),
    path('studentinfo/<int:one_id>/', StudentInfo.as_view()),
    path('testresultimage/<str:global_id>/',TestResultImage.as_view())
]

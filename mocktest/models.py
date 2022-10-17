from django.db import models
from teacher.models import Teacher
from teacher.models import Subject
from django.utils.translation import gettext_lazy as _
class BotUsers(models.Model):
    telegram = models.CharField(max_length=500,unique=True)
    fullname = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.fullname
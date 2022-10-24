from django.db import models

# Create your models here.
class BotUsers(models.Model):
    telegram = models.CharField(max_length=500,unique=True)
    fullname = models.CharField(max_length=500,null=True,blank=True)
    def __str__(self):
        return self.fullname
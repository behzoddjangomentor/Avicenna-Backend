from django.contrib import admin
# from mocktest.models import BotUsers
# Register your models here.
from url.models import BotUsers
admin.site.register(BotUsers)
from .models import *
admin.site.register(Davomat)
@admin.register(Tuitor)
class TuitorAdmin(admin.ModelAdmin):
    list_display = ['name','phone']
    search_fields = ['name','phone','about']
    list_per_page = 10
@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['tuitor']
    list_per_page = 10

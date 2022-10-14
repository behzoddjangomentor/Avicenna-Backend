from django.contrib import admin

# Register your models here.
from .models import Student,PaymentStudent
@admin.register(PaymentStudent)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['student','date']
    list_per_page = 10
    list_filter = ['date']
    search_fields = ['student__name']
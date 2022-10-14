from django.db import models

# Create your models here.
from students.models import Student
class PaymentStudent(models.Model):
    student =models.ForeignKey(Student,on_delete=models.CASCADE,related_name='paymentstudent')
    sum = models.CharField(max_length=600)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.student.name}ning to'lovi"
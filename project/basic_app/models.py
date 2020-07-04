from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    pics=models.ImageField(upload_to='pics',blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)
    Student_Report=models.FileField(upload_to='Student_Report',blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:list")

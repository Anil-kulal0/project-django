from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField('Student Name', max_length=50)
    division = models.CharField('Student class', max_length=50)
    
    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField('Teacher Name', max_length=50)
    rank = models.CharField('Teacher Rank', max_length=50)
    
    def __str__(self):
        return self.name

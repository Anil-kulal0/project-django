from django.db import models

# Create your models here.
class Cities(models.Model):
    city = models.CharField('City', max_length=50)
    
    def __str__(self):
        return self.city
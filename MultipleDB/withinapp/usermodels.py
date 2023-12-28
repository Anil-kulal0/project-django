from  django.db import models

class UserData(models.Model):
    name = models.CharField('Name',max_length=100)
    contact = models.CharField('Contact',max_length=10)
    
    
# class Cardata(models.Model):
#     modelname = models.CharField(' Model Name',max_length=100)
#     makeyear = models.CharField('Make Year',max_length=10)
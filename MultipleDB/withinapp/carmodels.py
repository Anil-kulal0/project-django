from django.db import models

class CarData(models.Model):
    modelname = models.CharField(' Model Name',max_length=100)
    makeyear = models.CharField('Make Year',max_length=10)
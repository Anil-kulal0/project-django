from django.db import models

# Create your models here.

class StudentData(models.Model):
    studentname = models.CharField('Student Name',max_length= 15)
    emailid = models.EmailField('Email_id',max_length=20)
    rollno = models.TextField('Roll No',max_length=5)
    contact = models.TextField('Contact',max_length=10)
    course = models.CharField('Course',max_length=20)
    bloodgroup = models.CharField('Blood Group',max_length=5)
        
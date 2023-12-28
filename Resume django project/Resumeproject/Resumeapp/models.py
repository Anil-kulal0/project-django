from django.db import models

# Create your models here.
STATE_CHOICE=(
      
      ('Andhra Pradesh'),	
       
      ('Arunachal Pradesh'),	
      ('Assam'),
      ('Bihar'),
      ('Chhattisgarh'),	
      ('Delhi'),
      ('Goa'	),
      ('Gujarat'),	
      ('Haryana'),	
      ('Himachal Pradesh'	),
      ('Jammu and Kashmir'),	
      ('Jharkhand'	),
      ('Karnataka'	),
      ('Madhya Pradesh'),	
      ('Maharashtra'),	
      ('Manipur'	),
      ('Mizoram'	),
      ('Nagaland'	),
      ('Odisha'	),
      ('Puducherry'),
      ('Punjab'	),
      ('Rajasthan'	),
      ('Sikkim'	),
      ('Tamil Nadu'),
      ('Telangana'	),
      ('Tripura'	),
      ('Uttar Pradesh')	,
      ('Uttarakhan'	),
      ('West Bengal'),
)

class Resume(models.Model):
      name = models.CharField('Name',max_length=100)
      dob = models.DateField('DOB',auto_now= False,auto_now_add=False)
      gender = models.CharField('Gender',max_length=100)
      locality = models.CharField('Locality',max_length=100)
      city = models.CharField('City',max_length=100)
      pin = models.IntegerField('Pin')
      state = models.CharField('State',choices= STATE_CHOICE, max_length=100)
      mobail = models.IntegerField('Mobail')
      email = models.EmailField('Email')
      job_city = models.CharField('Job City',max_length=100)
      profile_image = models.ImageField('Profile Image',upload_to='profileimg',blank=True)
      my_file = models.FileField('My File',upload_to='doc',blank=True)
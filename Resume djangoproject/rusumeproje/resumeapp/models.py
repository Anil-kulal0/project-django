from django.db import models

# Create your models here.


# Create your models here.
STATE_CHOICE=(
      ('Andhra Pradesh','Andhra Pradesh'),	 
      ('Arunachal Pradesh','Arunachal Pradesh'),	
      ('Assam','Assam'),
      ('Bihar','Bihar'),
      ('Chhattisgarh','Chhattisgarh'),	
      ('Delhi','Delhi'),
      ('Goa','Goa'),
      ('Gujarat','Gujarat'),	
      ('Haryana','Haryana'),	
      ('Himachal Pradesh','Himachal Pradesh'	),
      ('Jammu and Kashmir','Jammu and Kashmir'),	
      ('Jharkhand','Jharkhand'),
      ('Karnataka','Karnataka'),
      ('Madhya Pradesh','Madhya Pradesh'),	
      ('Maharashtra','Maharashtra'),	
      ('Manipur','Manipur'),
      ('Mizoram','Mizoram'),
      ('Nagaland'	,'Nagaland'),
      ('Odisha','Odisha'),
      ('Puducherry','Puducherry'),
      ('Punjab','Punjab'),
      ('Rajasthan','Rajasthan'),
      ('Sikkim','Sikkim'),
      ('Tamil Nadu','Tamil Nadu'),
      ('Telangana','Telangana'),
      ('Tripura','Tripura'),
      ('Uttar Pradesh','Uttar Pradesh')	,
      ('Uttarakhan','Uttarakhan'),
      ('West Bengal','West Bengal'),
)

Gender_choice=(
      ('Male','Male'),
      ('Female','Female')
)

Job_City_choice=(
      ('Pune','Pune'),
      ('Mumbai','Mumbai'),
      ('Delhi','Delhi'),
      ('Kolkatta','Kolkatta'),
      ('Ranchi','Ranchi')
)

class Resume(models.Model):
      name = models.CharField('Name',max_length=100)
      dob = models.DateField('DOB',auto_now= False,auto_now_add=False)
      gender = models.CharField('Gender', choices= Gender_choice, max_length=100)
      locality = models.CharField('Locality',max_length=100)
      city = models.CharField('City',max_length=100)
      pin = models.IntegerField('Pin')
      state = models.CharField('State',choices= STATE_CHOICE, max_length=100)
      mobile = models.IntegerField('Mobail')
      email = models.EmailField('Email')
      job_city = models.CharField('Job City', choices=Job_City_choice,max_length=100)
      profile_image = models.ImageField('Profile Image',upload_to='profileimg',blank=True)
      my_file = models.FileField('My File',upload_to='doc',blank=True)
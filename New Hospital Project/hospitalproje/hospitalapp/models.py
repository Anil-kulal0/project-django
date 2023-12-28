from django.db import models

# Create your models here.

class HospitalData(models.Model):
    hospital_name = models.CharField('Hospital Name',max_length=20)
    hospital_contact = models.IntegerField('Contact',max_length=10)
    hospital_address = models.TextField('Address',max_length=50)
    hospital_emailid = models.EmailField()
    hospital_specilization = models.CharField('Hospital Specilization',max_length=200)
    
    
    def __str__(self):
        
        return self.hospital_name    
    

class DocterData(models.Model):
    doctor_name = models.CharField('Doctor Name', max_length=50)
    doctor_specialiazation  = models.CharField('Specialiazation',max_length=200)
    doctor_doj = models.DateField('Date of Joining')
        
        
        
        
    def __str__(self):
            return self.doctor_name
        
    

class PatientData(models.Model):
    patient_name = models.CharField('Patient Name',max_length=50)
    patient_ward = models.CharField('Patient Ward',max_length=50)
    patient_age = models.IntegerField('Patient Age')
    patient_contact = models.IntegerField('Patient Contact')
    patient_address = models.TextField('Patient Address',max_length=200)
    patient_type = models.CharField('Patient Type',max_length=5)
    patient_doa = models.DateField('Date Of Addimission')
    patient_dod = models.DateField('Date Of Discharge')
    patient_hospital = models.ForeignKey(HospitalData,on_delete=models.CASCADE)
    patient_doctor = models.ForeignKey(DocterData, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.patient_name
        


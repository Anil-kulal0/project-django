from django import forms
from .models import HospitalData, DocterData, PatientData


class HospitalFrom(forms.ModelForm):
    class Meta:
        model = HospitalData
        fields = ['hospital_name','hospital_contact','hospital_address','hospital_emailid','hospital_specilization']

class DocterFrom(forms.ModelForm):
    class Meta:
        model = DocterData
        fields =['doctor_name','doctor_specialiazation','doctor_doj']
        
        
        
class PatientForm(forms.ModelForm):
    class Meta:
        model = PatientData
        fields =['patient_name','patient_ward','patient_age','patient_contact','patient_address','patient_type','patient_doa','patient_dod','patient_hospital','patient_doctor']
        
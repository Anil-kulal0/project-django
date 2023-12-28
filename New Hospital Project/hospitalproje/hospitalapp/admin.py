from django.contrib import admin
from .models import HospitalData, DocterData, PatientData 
 
# Register your models here.
admin.site.register(HospitalData)
admin.site.register(DocterData) 
admin.site.register(PatientData)
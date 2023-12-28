from django import forms
from .models import Resume


class ResumeForm(forms.ModelForm):
      class Meta:
            model = Resume
            fields = ['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']
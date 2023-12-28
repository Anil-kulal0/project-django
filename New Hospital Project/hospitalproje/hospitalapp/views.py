from django.shortcuts import render
from .forms import HospitalFrom, DocterFrom, PatientForm
from django.http import HttpResponseRedirect 
# Create your views here.
def registerhospital(request):
    if request.POST:
        form = HospitalFrom(request.POST)
        if form.is_valid():
            form.save()
            print('Data Save')
            return HttpResponseRedirect('/docter')
            
        
    form = HospitalFrom()
    return render (request,'hospitalregister.html', {'form' : form})
    
def Docter(request):
    if request.POST:
        form = DocterFrom(request.POST)
        if form.is_valid():
            form.save()
            print('Data Save')
            return HttpResponseRedirect('/patient')
    
    form = DocterFrom()
    return render (request, 'docterregister.html', { 'form' : form })


def Patient(request):
    if request.POST:
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            print('Data Save')
            return HttpResponseRedirect('/patient')
    
    form = PatientForm()
    return render (request, 'pantientregister.html', { 'form' : form })
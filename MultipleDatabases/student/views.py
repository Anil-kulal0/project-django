from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponseRedirect
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student/')
    form = StudentForm()
    return render (request, 'student/register.html', {'form':form})
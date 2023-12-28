from django.shortcuts import render
from .forms import TeacherForm
from django.http import HttpResponseRedirect
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teacher/')
    form = TeacherForm()
    return render (request, 'teacher/register.html', {'form':form})

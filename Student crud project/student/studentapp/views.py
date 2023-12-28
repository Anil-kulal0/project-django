from django.shortcuts import render

# Create your views here.

def register(request):
    if request.POST:
        studentname= request.POST['studentname']
        emailid = request.POST['emailid']
        rollno = request.POST[rollno]
        contact = request.POST['contact']
        course = request.POST['course']
        bloodgroup = request.POST['bloodgroup']
        
    return render (request,'register.html')
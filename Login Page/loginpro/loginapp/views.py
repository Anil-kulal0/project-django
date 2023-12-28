from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def signpage(request):
      if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password')
            password2 = request.POST.get('password2')
            
            #print(username,email,password1,password2)
            
            if password1!=password2:
                  return redirect('login') 
            
            else:          
                  my_user = User.objects.create(username=username,email=email,password=password1)
                  my_user.save()
                  return redirect('/')

                       
                  
            
            
      return render(request, 'signup.html')

def loginpage(request):
      if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            # print(username,password)
            user=authenticate(request, username=username, password=password)
            if user is not None:
                  login(request,user)
                  return redirect('home')
            else:
                  return redirect('/login')
      return render(request,'login.html')
@login_required(login_url='login')
def home(request):
      return render(request,'home.html')

def Logout(request):
      logout(request)
      return redirect('login')
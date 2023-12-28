from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request ,name):
    return HttpResponse(f'i am,{name}')
def get_age(request ,age):
    return HttpResponse(f'i am age,{age}')

def read_url_data(request):
    if 'name' in request.GET and 'age' in request.GET:  
        name=request.GET['name']
        age=request.GET['age'] 
        result = f'my name is{name},and my age is{age}'
        
    else:
       result=''
    return HttpResponse(result)

from datetime import datetime

def get_days(request, year, month, day):
    d1 = datetime.strptime(f'{year}-{month}-{day}', '%Y-%m-%d')
    d2 = datetime.today()
    ndays = (d2-d1).days
    from_date = d1.strftime('%Y-%m-%d')
    to_date = d2.strftime('%Y-%m-%d')
    
    result = f'From Date : {from_date} <br> \
        To Date : {to_date} <br> \
            Number of Days : {ndays}'
   
    return HttpResponse(result)

def addme(request,*args, **kwargs):
    #print(args,kwargs)
    a = kwargs.get('a')
    b = kwargs.get('b')
    result = f'Addition {a} and {b} = {a+b}'
    return HttpResponse(result)

def subme(request,*args, **kwargs):
    #print(args,kwargs)
    a = kwargs.get('a')
    b = kwargs.get('b')
    result = f'substraction {a} and {b} = {a-b}'
    return HttpResponse(result)

def mulme(request,*args, **kwargs):
    #print(args,kwargs)
    a = kwargs.get('a')
    b = kwargs.get('b')
    result = f'multipal {a} and {b} = {a*b}'
    return HttpResponse(result)

def divme(request,*args, **kwargs):
    #print(args,kwargs)
    a = kwargs.get('a')
    b = kwargs.get('b')
    result = f'divistion {a} and {b} = {a/b}'
    return HttpResponse(result)

def slugmessage(request,inputmsg):
    return HttpResponse(inputmsg)

def showname(request):
    if request.method == 'POST':
        name = request.POST['myname']
        #return render(request,'index.html', {'name': name})
        return HttpResponse(f'my name is {name}')
    else:
        name='NO Name'
        return render(request,'index.html', {'name': ''})
        #return HttpResponse(name)
    
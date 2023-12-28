from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import UserData
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def registeruser(request):
    if request.POST:
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        
        obj = UserData(name=name,contact=contact)
        obj.save(using='userdb')    
        
    
        dic = {'status' :'successfully Registered'}
        return JsonResponse(dic)
    
def showuser(request):
    obj = UserData.objects.all().using('userdb')
    datali = []
    for rec in obj:
        datali.append({'name':rec.name, 'contact':rec.contact})
    Jsondata = json.dumps(datali)
        
        
    return HttpResponse(Jsondata)
    # return JsonResponse(datali)
@csrf_exempt  
def registercar(request):
    pass

def showcar(request):
    pass
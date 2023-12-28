from django.shortcuts import render

# Create your views here.
def home(request):
      
      data={
            'list':['atul','anil','ashif','rohan','swastik','prajwal'],
            'numbers':[10,20,30,40,50,60,],
            'student_details':[
                  {'name':'Atul','phone':8080235873},
                  {'name':'Rohan','phone':9923567834},
                  {'name':'Ashif','phone':9843243488},
                  {'name':'Anil','phone':9284656082},
                  
                  
            ]
            
      }
      return render(request, 'index.html',data)

def calculator(request):
      c=''
      if request.method =='POST':
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr =request.POST.get('opr')
            if opr=='+':
                  c=n1+n2
            elif opr=='-':
                  c=n1-n2
            elif opr=='*':
                  c=n1*n2
            elif opr=='/':
                  c=n1/n2
                  
            else:
                  c='Invalid opr...'
            print(c)
      
      return render(request, 'calculator.html',{'c':c})

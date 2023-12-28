from django.shortcuts import render,HttpResponse
from .forms import ResumeForm
from .models import Resume
from django.views import View
# Create your views here.

class indexView(View):
      def get(self, request):
            form = ResumeForm()
            candidates = Resume.objects.all()
            return render(request,'index.html', { 'candidates':candidates, 'form': form})
      
      def post(self, request):
            form = ResumeForm(request.POST, request.FILES)
            
            # if form.is_valid():
            #       form.save()
            #       # return render(request,'index.html', {'form': form})
            if form.is_valid():
                        form.save()
                        return render(request,'index.html', {'form': form})
            
                  
                 
class candidateView(View):
      def get(self, request,pk):
            #print(pk)
            candidate = Resume.objects.get(pk=pk)
            return render(request,'candidate.html', {'candidate':candidate})
           
# def index(request):
#       return render(request,'index.html')
            
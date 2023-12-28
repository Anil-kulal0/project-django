from django.shortcuts import render
from .models import Cities
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    # obj = Cities.objects.all()
    paginate = Paginator(Cities.objects.all(), 2)
    pageno = request.GET.get('page')
    page_data = paginate.get_page(pageno)
    return render(request, 'home.html', {'Cities': page_data})

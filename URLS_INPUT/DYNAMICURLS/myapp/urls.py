"""DYNAMICURLS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>', views.home, name='home'),
    path('age/<str:age>', views.get_age, name='age'),
    path('getdetails/', views.read_url_data, name='getmethod'),
    path('daysbetweendates/<int:year>/<int:month>/<int:day>/', views.get_days, name='daysbetweendates'),
    path('addme/<int:a>/<int:b>', views.addme, name='getmethod'),
    path('subme/<int:a>/<int:b>', views.subme, name='getmethod'),
    path('mulme/<int:a>/<int:b>', views.mulme, name='getmethod'),
    path('divme/<int:a>/<int:b>', views.divme, name='getmethod'),

    path('simplemsg/<slug:inputmsg>', views.slugmessage, name='getmethod'),

    path('showname/', views.showname, name='showname'),
] 
   

  

from django.urls import path
from . import views

urlpatterns = [
    path('registeruser/',views.registeruser, name='registeruser'),
    path('showuser/',views.showuser, name='showuser'),
    path('registercar/',views.registercar, name='registercar'),
    path('showcar/',views.showcar, name='showcar'),
]
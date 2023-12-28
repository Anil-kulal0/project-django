
from django.urls import path

from . import views
urlpatterns = [
    path('', views.getRoutes, name='getRoutes'),
    path('notes/', views.getnotes, name='notes'),
    path('notes/create/', views.creatnotes, name='notes/create'),
    path('notes/<int:pk>/', views.getnote, name='notes'),
    path('notes/<int:pk>/update/', views.updatenote, name='notes/update'),
    path('notes/<int:pk>/delete/', views.deletenote, name='notes/delete'),
    path('note', views.getnote, name='notes'),

]

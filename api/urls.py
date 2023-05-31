from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.loadAPIPage, name='api'),
    path('create/', views.loadCreatePage, name='create'),
    
]
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='login'),
    path('register/', views.register, name='register'),
    path('example/', views.example, name='example')  
]
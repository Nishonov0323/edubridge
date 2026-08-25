from django.urls import path

from . import views

app_name = 'handbook'

urlpatterns = [
    path('', views.home, name='home'),
    path('module/<int:number>/', views.module_detail, name='module_detail'),
    path('itog/', views.integration, name='integration'),
]

from django.urls import path
from  ProfileApp import views
urlpatterns = [
    path('', views.home, name='home'),
    path('hello', views.helloword, name='hello'),
    path('firstpage', views.firstpage, name='firstpage'),
    path('secondpage', views.secondpage, name='secondpage'),
    path('thirdpage', views.thirdpage, name='thirdpage'),
    path('Hnypage', views.Hnypage, name='Hnypage'),
]
from django.urls import path
from ProductApp import views
urlpatterns = [
    path('testbt', views.testbt, name='testbt'),

]
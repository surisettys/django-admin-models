from django.urls import path
from urlapp import views

urlpatterns = [
     path('',views.stat,name ='stat')

]
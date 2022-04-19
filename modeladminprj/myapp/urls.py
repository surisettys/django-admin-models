
from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    
    path('add/',views.addstudent,name='add'),
    path('list/',views.liststudent,name='list'),
    path('delete/',views.deletestudent,name='delete')
]
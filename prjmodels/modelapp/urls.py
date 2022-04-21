from django.urls import path
from modelapp import views
urlpatterns = [
    path('',views.PatientView,name='patient')
]
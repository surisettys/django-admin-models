from django.shortcuts import render
from modelapp.models import Patient

# Create your views here.

def PatientView(request):

    patientlist = Patient.objects.all()
    context  = {'tag':patientlist}
    return render(request,'modelapp/patientview.html',context=context)

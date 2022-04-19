from django.shortcuts import render
from myapp.models import Student
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def index(request):

    return render(request,'myapp/base.html')

def addstudent(request):

    if request.POST:

        name = request.POST['name']
        age = request.POST['age']
        school = request.POST['school']

        Student.objects.create(name=name,age=age,school=school)
        return HttpResponseRedirect(reverse('myapp:list'))

    return render(request,'myapp/add.html')

def liststudent(request):

    studentlist = Student.objects.all()

    context = {'studentlist':studentlist}
    return render(request,'myapp/list.html',context = context)

def deletestudent(request):

    if request.POST:
        pk = request.POST['pk']

        try:
           Student.objects.get(pk=pk).delete()
           return HttpResponseRedirect(reverse('myapp:list'))
        except:
          return HttpResponse('Primary ket not available')

    return render(request,'myapp/delete.html')

    


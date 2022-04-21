from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return HttpResponse('<h1>This is index page</h1>')


newspaper = {'sports':'This is sports page',
            'et':'this is entertainment page',
            'fin':'this is financial page'}


def page(request,topic):

    return HttpResponse(newspaper[topic])

def adddview(request,num1,num2):

    sum = num1+num2

    return HttpResponse( f'The sum of {num1} and {num2} is = {sum}')

def redirectview(request,num_page):

    lst = list(newspaper.keys())
    topic = lst[num_page]
    return HttpResponseRedirect(reverse('page',args=[topic]))

def stat(request):

    return render(request,'urlapp/file.html')



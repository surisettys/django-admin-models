from django.shortcuts import render
from django.http import HttpResponse
from loginapp.models import Language,Book,BookInstance,Genre,Author
from django.views.generic import CreateView,DetailView
# Create your views here.

def index(request):
    return render(request,'loginapp/index.html')


def modelview(request):

    bookcount = Book.objects.all().count()
    authorcount = Author.objects.all().count()

    context = {'authorcount':authorcount,'bookcount':bookcount}

    return render(request,'loginapp/modelview.html',context=context)

class CreateBook(CreateView):

    model = Book
    fields = '__all__'

class BookDetail(DetailView):

    model = Book
    





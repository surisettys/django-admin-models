from django.db import models
from django.forms import CharField
from django.urls import reverse

# Create your models here.

class Genre(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):

        return f'The book genre is {self.name}'

class Language(models.Model):

    language = models.CharField(max_length=200)

    def __str__(self):
        return f'The book is written in {self.language}'

class Book(models.Model):

    title = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    language = models.ForeignKey(Language,on_delete=models.SET_NULL,null=True)
    isbn = models.CharField('ISBN',max_length=20,unique=True)
    summary = models.TextField(max_length=600)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('loginapp:book_detail',kwargs={"pk":self.pk})


class Author(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True,blank=True)

    class Meta:
        ordering = ['last_name','first_name']

    def get_absolute_url(self):

        return reverse('author_detail',kwargs={"pk":{self.pk}})

    def __str__(self):
        return f'{self.first_name},{self.last_name}'

import uuid

class BookInstance(models.Model):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey('Book',on_delete=models.RESTRICT,null=True)
    imprint = models,CharField(max_length=200)
    due_back = models.DateField()
    LOAN_STATUS= (
        ('m','Modified'),
        ('b','Borrowed'),
        ('o','On_Loan'),
    )
    status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} of ({self.book.title})'





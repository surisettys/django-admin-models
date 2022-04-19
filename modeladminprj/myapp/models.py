from django.db import models

# Create your models here.
class Student(models.Model):

    name = models.CharField(max_length=20)
    age = models.IntegerField()
    school = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name} of {self.age} belongs to {self.school}'

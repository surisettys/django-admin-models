from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class Patient(models.Model):

    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    disease = models.CharField(max_length=20)
    bp = models.IntegerField(default=60,validators=[MaxValueValidator(300),MinValueValidator(0)])

    def __str__(self):

        return f'{self.name} with {self.age} has {self.disease} has {self.bp}'

        

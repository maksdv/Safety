from django.db import models
from django.utils import timezone
from django import forms

class Chair(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    country = models.CharField(max_length=100)

class Item(models.Model):
    itemGroup = (
        ('0', 'Grupo 0'),
        ('0-1', 'Group 0-1'),
        ('1', 'Grupo 1'),
        ('2', 'Grupo 2-3'),
    )

    isofix = (
        ('si','si'),
        ('no', 'no'),
        )

    name = models.CharField(max_length=200)
    group = models.CharField(max_length=3, choices=itemGroup)
    score = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'static/images/', default = 'images/None/no-img.jpg')
    isofix = models.CharField(max_length=2, choices=isofix, default='si')

class Buscador(forms.Form):
    isofix = (
        ('si','si'),
        ('no', 'no'),
        )

    rang = (
        ('precio', 'Mejor precio'),
        ('calidad', 'Mejor opcón'),
        ('calpre', 'Calidad-Precio'),
        )

    edad = forms.IntegerField()
        




    def __str__(self):
        return self.name
        
    def __str__(self):
        return self.name


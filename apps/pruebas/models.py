from django.db import models

# Create your models here.

class Libros(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
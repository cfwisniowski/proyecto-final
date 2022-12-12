from django.db import models
from datetime import datetime

class Familiar(models.Model):

    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    numero_pasaporte = models.IntegerField()
    #creado_el = models.DateTimeField()
    #modificado_el = models.DateTimeField()
    #fecha_act = models.DateField()  #models.DateField()
  
def __str__(self):
  return f"{self.nombre}, {self.numero_pasaporte}, {self.id}, {self.direccion} {self.fecha_act}"


#input_formats=["%d-%m-%y"]
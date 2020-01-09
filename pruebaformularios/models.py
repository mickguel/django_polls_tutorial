from django.db import models
from django.forms import ModelForm

class Persona(models.Model):

    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=60)
    dni = models.IntegerField()
    direccion = models.CharField(max_length=100)
    email = models.EmailField()

    def __unicode__(self):
        return self.dni

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre','apellidos','dni','direccion','email']

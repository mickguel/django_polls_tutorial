from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Persona, PersonaForm

class PersonaList(ListView):

    model = Persona

def add_persona(request):
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = PersonaForm(request.POST) # Bound form
        if form.is_valid():
            new_persona = form.save() # Guardar los datos en la base de datos

            return HttpResponseRedirect(reverse('personas:plist'))
    else:
        form = PersonaForm() # Unbound form

    return render(request, 'pruebaformularios/persona_form.html', {'form': form})

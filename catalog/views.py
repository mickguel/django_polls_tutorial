from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Libros disponibles (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # El 'all()' esta implícito por defecto.

    #Addicional - Número de géneros y número libros con la palabra 'la'
    num_genres=Genre.objects.count()
    num_books_with_la=Book.objects.filter(title__icontains='la').count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_books':num_books,'num_instances':num_instances,
            'num_instances_available':num_instances_available,'num_authors':num_authors,
            'num_genres':num_genres,'num_books_with_la':num_books_with_la},
    )

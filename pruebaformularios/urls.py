from django.urls import path
from . import views

app_name = 'personas'
urlpatterns = [
    path('list/', views.PersonaList.as_view(), name='plist'),
    path('add/', views.add_persona, name='padd'),
]

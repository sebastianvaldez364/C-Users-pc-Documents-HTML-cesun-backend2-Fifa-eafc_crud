from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_cartas, name='lista_cartas'),

    path(
        'agregar/',
        views.agregar_carta,
        name='agregar_carta'
    ),

    path(
        'editar/<int:id>/',
        views.editar_carta,
        name='editar_carta'
    ),

    path(
        'eliminar/<int:id>/',
        views.eliminar_carta,
        name='eliminar_carta'
    ),
]
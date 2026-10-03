from django.shortcuts import render, redirect, get_object_or_404
from .models import Carta
from .forms import CartaForm


def lista_cartas(request):
    cartas = Carta.objects.all()

    return render(request, 'cartas/lista_cartas.html', {
        'cartas': cartas
    })


def agregar_carta(request):
    if request.method == 'POST':
        form = CartaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_cartas')
    else:
        form = CartaForm()

    return render(request, 'cartas/agregar_carta.html', {
        'form': form
    })


def editar_carta(request, id):
    carta = get_object_or_404(Carta, id=id)

    if request.method == 'POST':
        form = CartaForm(request.POST, instance=carta)

        if form.is_valid():
            form.save()
            return redirect('lista_cartas')
    else:
        form = CartaForm(instance=carta)

    return render(request, 'cartas/editar_carta.html', {
        'form': form,
        'carta': carta
    })


def eliminar_carta(request, id):
    carta = get_object_or_404(Carta, id=id)

    if request.method == 'POST':
        carta.delete()
        return redirect('lista_cartas')

    return render(request, 'cartas/eliminar_carta.html', {
        'carta': carta
    })
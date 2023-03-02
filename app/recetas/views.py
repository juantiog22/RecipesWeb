# recetas/views.py

from django.shortcuts import  HttpResponse, render, redirect
from recetas.models import  Receta
from .models import *
from recetas.forms import recetaForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index(request):
    return render(request,'index.html')

def busqueda(request):
    recetas = Receta.objects.all()
    return render(request,'busqueda.html', {'recetas':recetas})


##Permite consultar las recetas mediant el id       
def receta(request, receta_id):
    receta = Receta.objects.get(pk=receta_id)
    context = {'receta': receta}
    return render(request,'receta.html', context)

#Crea una nueva receta usando la clase form
def create(request):
    form = recetaForm()
    if request.method=="POST":
        form = recetaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Has añadido una receta!')
            return redirect('/busqueda')
    context = {'form':form}
    return render(request, 'create.html', context)

#Edita una receta usando la clase form pasando el id 
def editar(request, receta_id):
    receta = Receta.objects.get(pk=receta_id)
    form = recetaForm(instance=receta)
    if request.method == "POST":
        form = recetaForm(request.POST,request.FILES, instance=receta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Has editado una receta!')
            return redirect('/busqueda')
    context = {'form': form}
    return render(request, 'editar.html', context)


#Elimina una receta
def eliminarReceta(request, receta_id):
    receta = Receta.objects.get(id=receta_id)
    receta.delete()
    messages.success(request, 'Has eliminado una receta!')
    return redirect('/busqueda')

#Formulario para registrar un nuevo usuario
def register(request):
    if request.method == 'POST':
            form= UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                messages.success(request, f'Usuario {username} creado')
                return redirect('/')
    else:
        form = UserCreationForm()

    context = {'form':form}
    return render(request, 'register.html', context)


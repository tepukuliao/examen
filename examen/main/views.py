from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .forms import ModificarUser


def index(request):
    return render(request, 'index.html')

### register ###


def formulario(request):
    if request.method == 'GET':
        return render(request, 'formulario.html', {
            "form": CustomUserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                email=request.POST['email'], first_name=request.POST['first_name'],
                                                last_name=request.POST['last_name'], password=request.POST['password1'])
                user.save()
                return redirect('login')
            except IntegrityError:
                return render(request, 'formulario.html', {
                    "form": CustomUserCreationForm, "error": "Usuario ya existe"})

        return render(request, 'formulario.html', {
            "form": CustomUserCreationForm, "error": "Contraseñas no coinciden"})

### login logout ###


def inisesion(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            "form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {
                "form": AuthenticationForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('inicio')


def salir(request):
    logout(request)
    return redirect('inicio')

### Perfil ###

@login_required
def perfil(request):
    usuario_actual = request.user
    context = {
        'usuario': usuario_actual
    }
    return render(request, 'perfil.html', context)

### Modificar Eliminar ###

def eliminar(request, username):
    usuario = User.objects.get(username=username)

    try:
        usuario.delete()
        return redirect('inicio')

    except IntegrityError:
        return redirect('inicio')


def modificar(request, username):
    usuario = User.objects.get(username=username)
    
    if request.method == 'POST':
        form = ModificarUser(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, f'Usuario {username} modificado correctamente.')
            return redirect('perfil')  
    else:
        form = ModificarUser(instance=usuario)

    return render(request, 'modificar.html', {'form': form, 'usuario': usuario})

### items #######

def reptiles(request):
    return render(request,'items/reptiles.html')

def terrarios(request):
    return render(request,'items/terrarios.html')

def alimento(request):
    return render(request,'items/alimento.html')
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCliente.forms import ContactoForm, RegistroUsuarioForm, UserEditForm
from AppCliente.models import mensajes, usuario
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from .forms import RegistroUsuarioForm
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages



# Create your views here.
def inicioprin(request):
    return render(request, 'AppCliente/inicioprin.html')

def inicio(request):
    return render(request, 'AppCliente/inicio.html')


def selecuser(request):
    return render(request, "AppCliente/main.html")

def contacto(request):
    enviado = False

    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            enviado = True
            form = ContactoForm()  # limpiar el formulario
    else:
        form = ContactoForm()

    return render(request, "AppCliente/contacto.html", {"form": form, "enviado": enviado})


def categoria(request):
    return render(request, "AppCliente/categoria.html")


def catkitchen(request):
    return render(request, "AppCliente/catkitchen.html") 

def catliving(request):
    return render(request, "AppCliente/catliving.html")

def catbedroom(request):
    return render(request, "AppCliente/catbedroom.html")    

def catbathroom(request):
    return render(request, "AppCliente/catbathroom.html")  

def register(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()  # Crea el usuario en auth_user

            # Crea el objeto en tu modelo personalizado
            usuario.objects.create(
                user=user.username,
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                email=form.cleaned_data['email'],
                password=user.password,  # ya está hasheado
                telefono=form.cleaned_data['telefono'],
                direccion=form.cleaned_data['direccion'],
                ciudad=form.cleaned_data['ciudad'],
                codigo_postal=form.cleaned_data['codigo_postal'],
                fecha_nacimiento=form.cleaned_data['fecha_nacimiento'],
                fecha_registro=timezone.now().date()
            )

            return HttpResponse("Usuario creado exitosamente")
    else:
        form = RegistroUsuarioForm()
    return render(request, "AppCliente/registro.html", {"form": form})



def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario_login = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario_login, password=contra)

            if user is not None:
                login(request, user)
                return redirect('inicio')  # Redirige a la vista 'inicio'
            else:
                return render(request, "AppCliente/login.html", {
                    "form": form,
                    "mensaje": "Credenciales incorrectas"
                })
        else:
            return render(request, "AppCliente/login.html", {
                "form": form,
                "mensaje": "Formulario inválido"
            })
    else:
        form = AuthenticationForm()
        return render(request, "AppCliente/login.html", {"form": form})


def logout_request(request):
    logout(request)
    messages.success(request, "Sesión cerrada con éxito.")
    return redirect('inicioprin')  # o 'inicioprin', según tu flujo
 

def editarperfil( request ):
    usuario = request.user
    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion["email"]
            password = informacion["password1"]
            usuario.set_password(password)
            usuario.save()
            return render(request, "AppCliente/inicio.html")             
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    return render(request, "AppCliente/editar_perfil.html" ,{"miFormulario":miFormulario, "usuario":usuario})



    

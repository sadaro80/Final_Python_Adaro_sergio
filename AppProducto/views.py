from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm
from AppProducto.forms import ProductoFormulario
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login




def inicioproductos(request):
    return render(request, "AppProducto/lista_productos.html")


#def lista_productos(request):
    #productos = Producto.objects.all()
    #return render(request, "AppProducto/lista_productos.html", {"productos": productos})
def lista_productos(request, categoria=None):
    if categoria:
        productos = Producto.objects.filter(categoria__iexact=categoria)
    else:
        productos = Producto.objects.all()
    return render(request, "AppProducto/lista_productos.html", {"productos": productos})

    

def producto_formulario(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'AppProducto/formulario_producto.html', {'form': form})


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('lista_productos')


def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)

    if request.method == 'POST':
        form = ProductoFormulario(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')  # Asegurate de tener esta vista y ruta
    else:
        form = ProductoFormulario(instance=producto)

    return render(request, 'AppProducto/editar_producto.html', {'form': form})


def buscar_producto(request):
    return render(request , "AppProducto/buscar_producto.html")

def buscar(request):
    if request.POST["nombre"]:
        productos = Producto.objects.filter(nombre__icontains=request.POST["nombre"])
        return render(request, "AppProducto/resultado_busqueda.html", {"productos":productos})
    else:
        return HttpResponse("No se ha encontrado nada")
    
def login_admin_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario_login = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            user = authenticate(username=usuario_login, password=contra)

            if user is not None:
                login(request, user)
                return redirect('lista_productos')  # Redirige a la vista 'lista_productos'
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



def productos_por_categoria(request, categoria_nombre):
    productos = Producto.objects.filter(categoria__iexact=categoria_nombre)
    return render(request, 'AppCliente/catkitchen.html', {
        'productos': productos,
        'categoria': categoria_nombre.capitalize()
    })

def vista_productos(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'AppProducto/detalle.html', {'producto': producto})


def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    
    # Si ya está en el carrito, aumentamos la cantidad
    if str(producto_id) in carrito:
        carrito[str(producto_id)] += 1
    else:
        carrito[str(producto_id)] = 1

    request.session['carrito'] = carrito
    return redirect('vista_carrito')  # o redirigir a donde prefieras


def vista_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0

    for producto_id, cantidad in carrito.items():
        try:
            producto = Producto.objects.get(id=producto_id)
            producto.cantidad = cantidad
            producto.subtotal = producto.precio * cantidad
            total += producto.subtotal
            productos.append(producto)
        except Producto.DoesNotExist:
            continue

    return render(request, 'AppProducto/carrito.html', {'productos': productos, 'total': total})


def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    producto_id_str = str(producto_id)
    if producto_id_str in carrito:
        del carrito[producto_id_str]
        request.session['carrito'] = carrito

    return redirect('vista_carrito')


def vaciar_carrito(request):
    request.session['carrito'] = {}
    return redirect('vista_carrito')




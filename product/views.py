from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Product
from .forms import ProductForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    return render(request, "signup.html", {"form": UserCreationForm})


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "signin.html",
                {
                    "form": AuthenticationForm,
                    "error": "Usuario o la contraceña esta incorrecta",
                },
            )
        else: 
            login(request,user)
            return render(request, "products.html")


def signout(request):
    logout(request)
    return redirect("home")


def products(request):
    productos=Product.objects.all()
    return render(request, "products.html", {"productos":productos})

def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')  # Redirige a la lista de productos o a otra vista
    else:
        form = ProductForm()
    
    return render(request, 'new_product.html', {'form': form})

def update_product(request,id):
    producto = get_object_or_404(Product, id=id)  # Obtener el producto por su ID
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()  # Guardar los cambios
            return redirect('products')  # Redirigir a la página de detalles del producto
            # return redirect('detalle_producto', id=Product.id)  # Redirigir a la página de detalles del producto
    else:
        form = ProductForm(instance=producto)  # Cargar el formulario con los datos existentes del producto
    
    return render(request, 'update_product.html', {'form': form, 'producto': producto})


def detail_product(request, id):
    # Obtener el producto con el ID proporcionado, o lanzar un 404 si no se encuentra
    producto = get_object_or_404(Product, id=id)
    
    # Renderizar la plantilla con el producto encontrado
    return render(request, 'detail_product.html', {'producto': producto})

def delete_product(request, id):
    # Obtener el producto con el ID proporcionado, o lanzar un 404 si no se encuentra
    producto = get_object_or_404(Product, id=id)    

    if request.method == 'POST':
        producto.delete()  # Eliminar el producto
        return redirect('products')  # Redirigir a la lista de productos
    
    return render(request, 'delete_product.html', {'producto': producto})
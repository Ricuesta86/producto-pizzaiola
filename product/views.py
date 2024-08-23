from django.shortcuts import render, redirect
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

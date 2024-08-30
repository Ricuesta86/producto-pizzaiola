from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from .models import Product, Aggregate
from .forms import ProductForm, AggregateForm


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
            login(request, user)
            return redirect("products")


def signout(request):
    logout(request)
    return redirect("home")


@login_required(login_url="signin")
def products(request):
    productos = Product.objects.all()
    return render(request, "products/products.html", {"productos": productos})


@login_required(login_url="signin")
def new_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                "products"
            )  # Redirige a la lista de productos o a otra vista
    else:
        form = ProductForm()

    return render(request, "products/new_product.html", {"form": form})


@login_required(login_url="signin")
def update_product(request, id):
    producto = get_object_or_404(Product, id=id)  # Obtener el producto por su ID

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()  # Guardar los cambios
            return redirect(
                "products"
            )  # Redirigir a la página de detalles del producto
            # return redirect('detalle_producto', id=Product.id)  # Redirigir a la página de detalles del producto
    else:
        form = ProductForm(
            instance=producto
        )  # Cargar el formulario con los datos existentes del producto

    return render(
        request, "products/update_product.html", {"form": form, "producto": producto}
    )


@login_required(login_url="signin")
def detail_product(request, id):
    # Obtener el producto con el ID proporcionado, o lanzar un 404 si no se encuentra
    producto = get_object_or_404(Product, id=id)
    agregados = Aggregate.objects.filter(product=producto)

    # Renderizar la plantilla con el producto encontrado
    return render(
        request,
        "products/detail_product.html",
        {"producto": producto, "agregados": agregados},
    )


@login_required(login_url="signin")
def delete_product(request, id):
    # Obtener el producto con el ID proporcionado, o lanzar un 404 si no se encuentra
    producto = get_object_or_404(Product, id=id)

    if request.method == "POST":
        producto.delete()  # Eliminar el producto
        return redirect("products")  # Redirigir a la lista de productos

    return render(request, "products/delete_product.html", {"producto": producto})


@login_required(login_url="signin")
def generar_pdf_product(request, id):
    producto = Product.objects.get(id=id)  # Obtén el producto
    html_string = render_to_string("products/pdf_product.html", {"producto": producto})

    # Generar el PDF
    pdf_file = HTML(string=html_string).write_pdf()

    # Configurar la respuesta HTTP
    response = HttpResponse(pdf_file, content_type="application/pdf")
    response["Content-Disposition"] = (
        f'attachment; filename="producto_{producto.id}.pdf"'
    )

    return response


@login_required(login_url="signin")
def new_aggregate(request, producto_id):
    producto = get_object_or_404(Product, id=producto_id)
    agregados = producto.aggregates.all()

    if request.method == "POST":
        form = AggregateForm(request.POST)
        if form.is_valid():
            agregado = form.save(commit=False)
            agregado.product = producto
            agregado.save()
            return redirect("aggregate_new", producto_id=producto.id)
    else:
        form = AggregateForm()

    return render(
        request,
        "aggregates/detail_aggregate.html",
        {"form": form, "producto": producto, "agregados": agregados},
    )


@login_required(login_url="signin")
def update_aggregate(request, id):
    agregado = get_object_or_404(Aggregate, id=id)

    if request.method == "POST":
        form = AggregateForm(request.POST, instance=agregado)
        if form.is_valid():
            form.save()
            return redirect("products_detail", id=agregado.producto.id)
    else:
        form = AggregateForm(instance=agregado)

    return render(
        request,
        "aggregates/update_aggregate.html",
        {"form": form, "agregado": agregado},
    )


@login_required(login_url="signin")
def delete_aggregate(request, id, producto_id):
    agregado = get_object_or_404(Aggregate, id=id)
    agregado.delete()
    return redirect("aggregate_new", producto_id=producto_id)
    # if request.method == 'POST':
    #     agregado.delete()
    #     return redirect('aggregate_new', producto_id=producto_id)
    # else:
    #     form = AggregateForm()

    # return render(request, 'aggregates/detail_aggregate.html', {'form': form, 'producto': producto, 'agregados':agregados})

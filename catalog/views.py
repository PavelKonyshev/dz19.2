from django.shortcuts import render,get_object_or_404
from .models import Category, Product

def home(request):
    products = Product.objects.all()
    context = {'product': products}
    return render(request, "product.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "contacts.html")

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'products': product}
    return render(request, "product_detail.html", context)



# Create your views here.

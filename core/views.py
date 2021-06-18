from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def category_detail_view(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "detail.html", {'name': category.name, 'title': str(category.name)})


def product_detail_view(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "detail.html", {'name': product.name, 'title': str(product.name)})

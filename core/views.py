from django.shortcuts import render
from rest_framework import generics

from .serialzers import ProductSerializer, CategorySerializer
from .models import Product, Category


# Create your views here.


def category_detail_view(request, pk):
    category = Category.objects.get(id=pk)
    return render(request, "detail.html", {'name': category.name, 'title': str(category.name)})


def product_detail_view(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "detail.html", {'name': product.name, 'title': str(product.name)})


class ProductDetailAPIView(generics.RetrieveAPIView):
    """
    Detail view for Product
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryDetailAPIView(generics.RetrieveAPIView):
    """
    Detail view for Category
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(generics.ListAPIView):
    """
    Defines the List behaviour of our rest api.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListView(generics.ListAPIView):
    """
    Defines the List behaviour of our rest api.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductCreateView(generics.CreateAPIView):
    """
    Defines the create behaviour of our rest api.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        """
        Save the post data when creating a new product.
        """

        serializer.save()


class CategoryCreateView(generics.CreateAPIView):
    """
    Defines the create behaviour of our rest api.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        """
        Save the post data when creating a new product.
        """

        serializer.save()

# class ProductUpdateView(generics.UpdateAPIView):
#     """
#     Defines the Update behaviour of our rest api.
#     """

#     queryset = Product.objects.
#     serializer_class = CategorySerializer
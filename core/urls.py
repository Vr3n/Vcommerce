from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import category_detail_view, product_detail_view, ProductCreateView, CategoryCreateView, CategoryListView, ProductListView

urlpatterns = [
    path('product/<int:pk>', product_detail_view, name="product_detail"),
    path('category/<int:pk>', category_detail_view, name="category_detail"),

    path('product_create/', ProductCreateView.as_view(), name="product_create"),
    path('products/', ProductListView.as_view(), name="product_list"),
    
    path('category_create/', CategoryCreateView.as_view(), name="category_create"),
    
    path('categories/', CategoryListView.as_view(), name="category_list"),
]

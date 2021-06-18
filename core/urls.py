from django.urls import path
from .views import category_detail_view, product_detail_view

urlpatterns = [
    path('product/<int:pk>', product_detail_view, name="product"),
    path('category/<int:pk>', category_detail_view, name="category"),
]
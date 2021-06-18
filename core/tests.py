from django.test import TestCase
from django.urls import reverse
from .models import Product, Category
import requests

# Create your tests here.


class CategoryTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="test category")

    def test_string_representation(self):
        self.assertEqual(str(self.category), self.category.name)

    def test_created_properly(self):
        self.assertEqual(self.category.name, "test category")

    def test_absolute_url(self):
        self.assertEqual(self.category.get_absolute_url(),
                         reverse('category', args=[self.category.id]))


class ProductTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        r = requests.get("https://fakestoreapi.com/products")
        data = r.json()
        cls.category = Category.objects.create(name="test category")
        cls.product_name = data[0]['title']
        cls.product_price = float(data[0]['price'])
        cls.product_description = data[0]['description']
        cls.product_image_url = data[0]['image']
        cls.product = Product.objects.create(
            name=data[0]['title'],
            price=float(data[0]['price']),
            description=data[0]['description'],
            image_url=data[0]['image'],
        )

    def test_string_representation(self):
        self.assertEqual(str(self.product),
                         f"{self.product.name} - {self.product.price}")

    def test_created_properly(self):
        self.assertEqual(self.product.name, self.product_name)

    def test_category_added_properly(self):
        self.product.category.add(self.category)
        self.assertEqual(self.product.category.first().name,
                         self.category.name)

    def test_absolute_url(self):
        self.assertEqual(self.product.get_absolute_url(),
                         reverse('product', args=[self.product.id]))

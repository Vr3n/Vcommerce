from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Product, Category
import requests


class CategoryAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.category_api = {
            "name": "API Category"
        }
        self.response = self.client.post(
            reverse('category_create'),
            self.category_api,
            format="json"
        )
        self.categories = Category.objects.all()

    def test_api_can_create_a_category(self):
        """
        Test that api can create a category.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_list_categories(self):
        """
        Test that api can list categories.
        """

        response = self.client.get(
            reverse('category_list'),
            format="json"
        )
        list_count = response.json()
        self.assertEqual(list_count['count'], self.categories.count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProductAPITest(TestCase):

    @classmethod
    def setUpTestData(cls):
        r = requests.get("https://fakestoreapi.com/products")
        cls.data = r.json()

    def setUp(self):
        self.client = APIClient()
        self.product_json = {
            "name": self.data[0]['title'],
            "price": float(self.data[0]['price']),
            "description": self.data[0]['description'],
            "image_url": self.data[0]['image'],
            "category": self.data[0]['category']
        }
        self.response = self.client.post(
            path=reverse('product_create'),
            data=self.product_json,
            format="json"
        )

        self.products = Product.objects.all()

    def test_api_can_create_a_product(self):
        """
        Test that api can create a Product.
        """

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_list_products(self):
        """
        Test that api can list products.
        """

        response = self.client.get(
            reverse('product_list'),
            format="json"
        )
        list_count = response.json()
        self.assertEqual(list_count['count'], self.products.count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

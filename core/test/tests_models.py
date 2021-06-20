from django.test import TestCase
from django.urls import reverse
from ..models import Product, Category, Cart
import requests

# Create your tests here.


class CategoryTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="test category")
        cls.category_2 = Category(name="Test 2 Category")

    def test_model_can_create_a_category(self):
        """
        Test that Category model can create a Category.
        """
        old_count = Category.objects.count()
        self.category_2.save()
        new_count = Category.objects.count()
        self.assertGreater(new_count, old_count)

    def test_string_representation(self):
        """
        Testing the String representation of model.
        """
        self.assertEqual(str(self.category), self.category.name)

    def test_created_properly(self):
        """
        Test for model data inserted properly
        """
        self.assertEqual(self.category.name, "test category")

    def test_absolute_url(self):
        """
        Testing the get_absolute_url method of model.
        """
        self.assertEqual(self.category.get_absolute_url(),
                         reverse('category_detail', args=[self.category.id]))


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
        cls.product_2 = Product(
            name=data[3]['title'],
            price=float(data[3]['price']),
            description=data[3]['description'],
            image_url=data[3]['image'],
        )
        cls.api_test_data = data[2:8]

    def test_model_can_create_a_product(self):
        """
        Test that Product model can create a Product.
        """

        old_count = Product.objects.count()
        self.product_2.save()
        new_count = Product.objects.count()
        self.assertGreater(new_count, old_count)

    def test_string_representation(self):
        """
        Testing the String representation of model.
        """

        self.assertEqual(str(self.product),
                         f"{self.product.name} - {self.product.price}")

    def test_created_properly(self):
        """
        Test that Category model can create a Category.
        """

        self.assertEqual(self.product.name, self.product_name)

    def test_category_added_properly(self):
        """
        Test for model data inserted properly
        """

        self.product.category.add(self.category)
        self.assertEqual(self.product.category.first().name,
                         self.category.name)

    def test_absolute_url(self):
        """
        Testing the get_absolute_url method of model.
        """

        self.assertEqual(self.product.get_absolute_url(),
                         reverse('product_detail', args=[self.product.id]))


class CartTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        r = requests.get("https://fakestoreapi.com/products")
        data = r.json()
        for i in range(len(data)):
            Product.objects.create(
                name=data[i]['title'],
                price=float(data[i]['price']),
                description=data[i]['description'],
                image_url=data[i]['image'],
            )

        products = Product.objects.all()[1:11]
        cls.ten_products = Product.objects.all()[12:22]
        Cart.product.add(products)

    def test_add_products_to_cart(self):
        old_cart_count = Cart.objects.count()
        product = Product.objects.get(id=22)
        Cart.product.add(product)
        new_cart_count = Cart.objects.count()
        self.assertGreater(new_cart_count, old_cart_count)
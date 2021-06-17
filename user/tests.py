from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.


class UserManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            email="normal@user.com", password="testing@123")
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:

            self.assertIsNotNone(user.username)
            self.assertIsNotNone(user.email)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="testing@123")

    def test_create_superuser(self):
        User = get_user_model()
        admin = User.objects.create_superuser(
            email="admin@user.com", password="testing@123")
        self.assertEqual(admin.email, 'admin@user.com')
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        try:
            self.assertIsNotNone(admin.username)
            self.assertIsNotNone(admin.email)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_user(
                email='', password="testing@123", is_superuser=False)

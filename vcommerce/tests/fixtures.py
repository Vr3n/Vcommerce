import pytest


@pytest.fixture
def create_admin_user(django_user_model):
    """
    Return new admin user.
    """

    return django_user_model.objects.create_superuser(username="admin",
                                                      email="a@a.com",
                                                      password="password")

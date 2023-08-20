import pytest
from inventory import models


@pytest.fixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (2, "trainers", "trainers", 1),
        (3, "baseball", "baseball", 1),
    ]
)
def test_inventory_category_dbfixture(
    db, django_db_fixture_setup, id, name, slug, is_active
):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.parametrize(
    "slug, is_active",
    [
        ("fashion", 1),
        ("trainers", 1),
        ("baseball", 1),
    ]
)
def test_inventory_db_category_insert_data(
    db, category_factory, slug, is_active
):
    result = category_factory.create(slug=slug, is_active=is_active)
    assert result.slug == slug
    assert result.is_active == is_active

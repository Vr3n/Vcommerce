import pytest
from inventory import models
from django.db import IntegrityError


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, name, slug, is_active",
    [
        (1, "fashion", "fashion", 1),
        (18, "trainers", "trainers", 1),
        (35, "baseball", "baseball", 1),
    ],
)
def test_inventory_category_dbfixture(
    db, django_db_fixture_setup, id, name, slug, is_active
):
    result = models.Category.objects.get(id=id)
    assert result.name == name
    assert result.slug == slug
    assert result.is_active == is_active


@pytest.mark.dbfixture
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


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, web_id, name, slug, description, is_active, created_at, updated_at",
    [
        (
            1,
            "45425810",
            "widstar running sneakers",
            "widstar-running-sneakers",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            1,
            "2022-01-01 14:18:33",
            "2022-01-01 14:18:33",
        ),
        (
            8616,
            "45434425",
            "impact puse dance shoe",
            "impact-puse-dance-shoe",
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin porta, eros vel sollicitudin lacinia, quam metus gravida elit, a elementum nisl neque sit amet orci. Nulla id lorem ac nunc cursus consequat vitae ut orci. In a velit eu justo eleifend tincidunt vel eu turpis. Praesent eu orci egestas, lobortis magna egestas, tincidunt augue. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean vitae lectus eget tortor laoreet efficitur vel et leo. Maecenas volutpat eget ante id tempor. Etiam posuere ex urna, at aliquet risus tempor eu. Aenean a odio odio. Nunc consectetur lorem ante, interdum ultrices elit consectetur sit amet. Vestibulum rutrum interdum nulla. Cras vel mi a enim eleifend blandit. Curabitur ex dui, rutrum et odio sit amet, auctor euismod massa.",
            1,
            "2022-01-01 14:18:33",
            "2022-01-01 14:18:33",
        ),
    ],
)
def test_inventory_db_product_dbfixture(
    db,
    django_db_fixture_setup,
    id,
    web_id,
    name,
    slug,
    description,
    is_active,
    created_at,
    updated_at,
):
    result = models.Product.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.web_id == web_id
    assert result.name == name
    assert result.slug == slug
    assert result.description == description
    assert result.is_active == is_active
    assert result_created_at == created_at
    assert result_updated_at == updated_at


@pytest.mark.dbfixture
def test_inventory_db_product_uniqueness_integrity(db, product_factory):
    new_web_id = product_factory.create(web_id=123456789)
    with pytest.raises(IntegrityError):
        product_factory.create(web_id=123456789)


@pytest.mark.dbfixture
def test_inventory_db_product_insert_data(
    db, product_factory, category_factory
):
    new_product = product_factory.create(category=(1, 2))
    result_product_category = new_product.category.all().count()
    assert "web_id_" in new_product.web_id
    assert result_product_category == 2


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    "id, sku, upc, product_type, product, brand, is_active, retail_price, store_price, sale_price, weight, created_at, updated_at",
    [
        (
            1,
            "7633969397",
            "934093051374",
            1,
            1,
            1,
            1,
            97.00,
            92.00,
            46.00,
            987,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
        (
            8616,
            "3880741573",
            "844935525855",
            1,
            8616,
            1253,
            1,
            89.00,
            84.00,
            42.00,
            929,
            "2021-09-04 22:14:18",
            "2021-09-04 22:14:18",
        ),
    ],
)
def test_inventory_db_product_inventory_dataset(
    db,
    django_db_fixture_setup,
    id,
    sku,
    upc,
    product_type,
    product,
    brand,
    is_active,
    retail_price,
    store_price,
    sale_price,
    weight,
    created_at,
    updated_at,
):
    result = models.ProductInventory.objects.get(id=id)
    result_created_at = result.created_at.strftime("%Y-%m-%d %H:%M:%S")
    result_updated_at = result.updated_at.strftime("%Y-%m-%d %H:%M:%S")
    assert result.sku == sku
    assert result.upc == upc
    assert result.product_type.id == product_type
    assert result.product.id == product
    assert result.brand.id == brand
    assert result.is_active == is_active
    assert result.retail_price == retail_price
    assert result.store_price == store_price
    assert result.sale_price == sale_price
    assert result.weight == weight
    assert result_created_at == created_at
    assert result_updated_at == updated_at


def test_inventory_db_product_inventory_insert_data(
    db, product_inventory_factory
):
    new_product = product_inventory_factory.create(
        sku="123456789",
        upc="123456789",
        product_type__name="new_name",
        product__web_id="123456789",
        brand__name="new_name",
    )
    assert new_product.sku == "123456789"
    assert new_product.upc == "123456789"
    assert new_product.product_type.name == "new_name"
    assert new_product.product.web_id == "123456789"
    assert new_product.brand.name == "new_name"
    assert new_product.is_active == 1
    assert new_product.retail_price == 97.00
    assert new_product.store_price == 92.00
    assert new_product.sale_price == 46.00
    assert new_product.weight == 987
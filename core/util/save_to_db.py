import requests
from ..models import Category, Product


# r = requests.get('https://fakestoreapi.com/products')

# data = r.json()


def save_to_db(data):

    for p in data:

        product_name = p['title']
        product_price = float(p['price'])
        product_description = p['description']
        product_image_url = p['image']

        product = Product.objects.create(
            name=product_name,
            price=product_price,
            description=product_description,
            image_url=product_image_url
        )

        category = p['category']

        
        cat = Category.objects.get_or_create(name=category)

        product.category.add(cat[0].id)


# abc

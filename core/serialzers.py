from rest_framework import serializers
from .models import Category, Product

# Create your serializers here.


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        many=True, view_name='category_detail', read_only=True)
    url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Product
        fields = [
            'url',
            'name',
            'price',
            'description',
            'image_url',
            'category',
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Category
        fields = [
            'url',
            'name'
        ]

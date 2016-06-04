from apps.products.models import Product
from rest_framework import serializers
from apps.news.serializers import NewsSerializer


class ProductSerializer(serializers.ModelSerializer):
    news = NewsSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'url', 'name', 'version', 'product', 'news')

# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')

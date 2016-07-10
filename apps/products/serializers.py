from apps.news.models import News
from apps.products.models import Product
from rest_framework import serializers
from apps.news.serializers import NewsSerializer


class ProductSerializer(serializers.ModelSerializer):
    news = NewsSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'url', 'name', 'version', 'product', 'news')

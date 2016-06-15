from apps.news.models import News
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'version', 'changes')

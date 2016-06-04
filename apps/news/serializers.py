from apps.news.models import News, VersionChange
from rest_framework import serializers


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'version')


class VersionChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionChange
        fields = ('id', 'info')
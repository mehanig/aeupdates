from django.contrib import admin
from apps.news.models import News, VersionChange


admin.site.register(News)
admin.site.register(VersionChange)
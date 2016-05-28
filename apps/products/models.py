from django.db import models
from apps import news as news


class Product(models.Model):
    url = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    version = models.CharField(max_length=128)
    product = models.CharField(max_length=128, blank=True)
    news = models.ManyToManyField('news.News')

    objects = models.Manager()

    def __str__(self):
        return 'Product: {}'.format(self.name)

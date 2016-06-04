from django.db import models


# TODO: product field should be blank=False! change asap
class Product(models.Model):
    url = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    version = models.CharField(max_length=128)
    product = models.CharField(max_length=128, blank=True)
    news = models.ManyToManyField('news.News', blank=True)

    objects = models.Manager()

    def __str__(self):
        return 'Product: {}'.format(self.name)

from django.db import models
from ..products.models import Product

class News(models.Model):
    version = models.CharField(max_length=128)
    changes = models.TextField(blank=False)
    origin = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+', default=None)

    objects = models.Manager()

    def __str__(self):
        return 'NewsObject: {}, with changes: {}...'.format(self.version, self.changes[:100])

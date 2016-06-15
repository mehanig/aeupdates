from django.db import models


class News(models.Model):
    version = models.CharField(max_length=128)
    changes = models.TextField(blank=False)
    objects = models.Manager()

    def __str__(self):
        return 'NewsObject: {}, with changes: {}...'.format(self.version, self.changes[:100])
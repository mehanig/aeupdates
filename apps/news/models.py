from django.db import models


class News(models.Model):
    version = models.CharField(max_length=128)
    changes = models.CharField(max_length=1024)

    objects = models.Manager()

    def __str__(self):
        return 'NewsObject: {}'.format(self.name)



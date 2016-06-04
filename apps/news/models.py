from django.db import models


class News(models.Model):
    version = models.CharField(max_length=128)
    changes = models.ManyToManyField('news.VersionChange', blank=True)
    objects = models.Manager()

    def __str__(self):
        return 'NewsObject: {}, with changes: {}'.format(self.version, self.changes.all())


class VersionChange(models.Model):
    info = models.CharField(max_length=1024, blank=False)

    objects = models.Manager()

    def __str__(self):
        return 'VersionChangeObject: {}'.format(self.info)
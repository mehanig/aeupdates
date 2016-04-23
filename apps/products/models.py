from django.db import models

# Create your models here.

# class ProductManager(models.Manager):
#     pass


class Product(models.Model):
    url = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    version = models.CharField(max_length=128)
    # news: DS.hasMany('news-item')

    objects = models.Manager()
    # class Meta:
    #     unique_together = ['user', 'target_type', 'target_id']
    #     index_together = [('target_type', 'target_id')]
    #     ordering = ['-id']
    #
    #
    # def __str__(self):
    #     return '{user}: {poll} on {target}'.format(
    #         user=self.user, poll=self.get_poll_display(), target=self.target
    #     )

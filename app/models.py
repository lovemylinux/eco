from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField()
    CATEGORY = (
        ('T', 'Travel'),
        ('A', 'Addiction')
    )
    category = models.CharField(default='T', max_length=1, choices=CATEGORY)
    image = models.ImageField(upload_to='media')


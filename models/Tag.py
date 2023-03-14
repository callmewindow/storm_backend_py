from django.conf import settings
from django.db import models
from django.utils.timezone import now

class Blog(models.Model):
    name = models.CharField('标签名', max_length=10)

    class Meta:
        db_table = 'tag'
        
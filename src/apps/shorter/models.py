# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
import string
import random
from django.conf import settings


CHARSET = getattr(settings, 'SHORTENER_CHARSET', string.ascii_letters + string.digits)
LENGTH = getattr(settings, 'SHORTENER_LENGTH', 8)


def url_generator():
    return ''.join(random.choice(CHARSET) for x in range(LENGTH))


class UrlShorter(models.Model):
    url = models.URLField(max_length=512)
    url_short = models.URLField(max_length=6, unique=True)
    user = models.ForeignKey(User, related_name='urls', on_delete=CASCADE)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            url_short = url_generator()
            while UrlShorter.objects.filter(url_short=url_short).exists():
                url_short = url_generator()
            self.url_short = url_short
        super(UrlShorter, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Short Link"
        verbose_name_plural = "Short Links"
        ordering = ('created_at',)
        get_latest_by = 'created_at'

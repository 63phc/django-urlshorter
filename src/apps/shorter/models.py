# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.urls import reverse
from .utils import create_urlshort


class ShortenUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(ShortenUrlManager, self).all(*args, **kwargs)
        return qs


class UrlShorter(models.Model):
    url = models.URLField(max_length=512)
    url_short = models.URLField(max_length=6, unique=True)
    user = models.ForeignKey(User, related_name='urls', on_delete=CASCADE)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = ShortenUrlManager()

    def save(self, *args, **kwargs):
        if self.url_short is None or self.url_short == "":
            self.url_short = create_urlshort(self)
        super(UrlShorter, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse("url_short", kwargs={'url_short': self.url_short, })
        return url_path

    class Meta:
        verbose_name = "Short Link"
        verbose_name_plural = "Short Links"
        ordering = ('-created_at',)

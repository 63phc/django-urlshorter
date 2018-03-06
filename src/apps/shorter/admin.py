# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from apps.shorter.models import UrlShorter

admin.site.register(UrlShorter)

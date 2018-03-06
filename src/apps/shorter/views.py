# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404

from django.utils.decorators import method_decorator
from django.views import View

from apps.shorter.models import UrlShorter


@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class IndexView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


# def redirect(request, url_short):
#     url_short = get_object_or_404(UrlShorter, pk=url_short)
#     url_short.count += 1
#     url_short.save()
#     return HttpResponseRedirect(url_short.url)


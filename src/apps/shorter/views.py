# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render, get_object_or_404
from django.template.context_processors import csrf
from django.utils.decorators import method_decorator
from django.views import View

from apps.shorter.form import UrlShorterForm
from apps.shorter.models import UrlShorter


@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class IndexView(View):

    def get(self, request):
        form = UrlShorterForm()
        urls = UrlShorter.objects.filter(user=request.user)
        context = {'urls': urls, 'urlshorter_form': form}
        context.update(csrf(request))
        return render_to_response('shorter/index.html', context)

    def post(self, request, *args, **kwargs):
        form = UrlShorterForm(request.POST)
        template = 'shorter/index.html'
        context = {'form': form, }
        if form.is_valid():
            url = form.cleaned_data.get("url")
            user = request.user
            obj, created = UrlShorter.objects.get_or_create(url=url, user=user)
            context = {'object': obj}
            if created:
                template = 'shorter/success.html'
            else:
                template = 'shorter/already-exists.html'
        return render(request, template, context)


class UrlShorterRedirect(View):
    def get(self, request, url_short=None, *args, **kwargs):
        print(url_short)
        short_link = get_object_or_404(UrlShorter, url_short=url_short)
        short_link.count = F('count') + 1
        short_link.save()
        return HttpResponseRedirect(short_link.url)

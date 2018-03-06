# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.template.context_processors import csrf
from django.utils.decorators import method_decorator
from django.views import View

from apps.shorter.form import UrlShorterForm
from apps.shorter.models import UrlShorter


@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class IndexView(View):

    def return_form(self, request, form):
        context = {'urlshorter_form': form}
        context.update(csrf(request))
        return render_to_response('shorter/index.html', context)

    def get(self, request):
        return self.return_form(request, UrlShorterForm())

    def post(self, request, *args, **kwargs):
        form = UrlShorterForm(request.POST)
        template = 'shorter/index.html'
        context = {'form': form, }
        if form.is_valid():
            print(form.cleaned_data)
            url = form.cleaned_data.get("url")
            user = request.user
            obj, created = UrlShorter.objects.get_or_create(url=url, user=user)
            context = {'object': obj}
            if created:
                template = 'shorter/success.html'
            else:
                template = 'shorter/already-exists.html'
        return render(request, template, context)


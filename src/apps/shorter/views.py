from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, redirect
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
        if form.is_valid():
            url = form.cleaned_data.get("url")
            user = request.user
            obj, created = UrlShorter.objects.get_or_create(url=url, user=user)
        return redirect('index')


class UrlShorterRedirect(View):

    def get(self, request, url_short=None):
        short_link = get_object_or_404(UrlShorter, url_short=url_short)
        short_link.count = F('count') + 1
        short_link.save()
        return HttpResponseRedirect(short_link.url)



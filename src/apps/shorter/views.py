from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views import View

from apps.shorter.form import UrlShorterForm
from apps.shorter.utils import url_generator
from apps.shorter.models import UrlShorter


@method_decorator(login_required(login_url='/auth/login/'), name='dispatch')
class IndexView(View):

    def get(self, request):
        form = UrlShorterForm()
        urls = UrlShorter.objects.filter(user=request.user)
        context = {'urls': urls, 'urlshorter_form': form}
        return render(request, 'shorter/index.html', context)

    def post(self, request, *args, **kwargs):
        form = UrlShorterForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get("url")
            user = request.user
            if not UrlShorter.objects.filter(url=url, user=user).exists():
                UrlShorter.objects.create(url=url, user=user, url_short=url_generator())
                messages.success(request, 'Link successfully added.')
            else:
                messages.info(request, 'That link is already exist.')
        else:
            for field, errors in form.errors.as_data().items():
                for error in errors:
                    if error.code == 'required':
                        field_label = form.fields[field].label
                        messages.error(request, 'Field "{}" is required.'.format(field_label))
                    if error.code == 'invalid':
                        messages.error(request, error.message)

        return redirect('index')


class UrlShorterRedirect(View):

    def get(self, request, url_short):
        short_link = get_object_or_404(UrlShorter, url_short=url_short)
        short_link.count += 1
        short_link.save()
        return HttpResponseRedirect(short_link.url)



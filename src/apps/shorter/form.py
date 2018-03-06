from django import forms


class UrlShorterForm(forms.Form):
    url = forms.URLField(label='URL you would like to shorten', required=True)

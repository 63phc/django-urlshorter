import random
import string
from django.conf import settings

URLSHORT_MIN = getattr(settings, "URLSHORT_MIN", 6)


def url_generator(size=URLSHORT_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_urlshort(instance, size=URLSHORT_MIN):
    new_code = url_generator(size=size)
    model_class = instance.__class__
    qs = model_class.objects.filter(url_short=new_code)
    if qs.exists():
        return create_urlshort(size=size)
    return new_code

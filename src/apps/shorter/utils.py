import random
import string


def url_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def create_urlshort(instance, size=6):
    new_code = url_generator(size=size)
    model_class = instance.__class__
    qs = model_class.objects.filter(url_short=new_code)
    if qs.exists():
        return create_urlshort(size=size)
    return new_code

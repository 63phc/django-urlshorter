from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


class UrlShorter(models.Model):
    url = models.URLField(max_length=512)
    url_short = models.CharField(max_length=6, unique=True)
    user = models.ForeignKey(User, related_name='urls', on_delete=CASCADE)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.url)

    class Meta:
        verbose_name = "Short Link"
        verbose_name_plural = "Short Links"
        ordering = ('-created_at',)

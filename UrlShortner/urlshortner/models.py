from django.db import models
import random
import string
from datetime import timedelta
from django.utils import timezone
# Create your models here.
class URLShortnerManager(models.Manager):

    def active_urls(self):
        return self.filter(
            is_expired=False
        ).filter(
            models.Q(expires_at__isnull=True) |
            models.Q(expires_at__gt=timezone.now())
        )
class URLShortner(models.Model):
    original_url = models.URLField(max_length=200)
    short_url = models.CharField(max_length=50,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null = True, blank = True)
    is_expired = models.BooleanField(default=False)
    clicks = models.IntegerField(default=0)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)


    objects = URLShortnerManager()

    @staticmethod
    def generate_short_url():
        length = 6
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(length))
        return short_url
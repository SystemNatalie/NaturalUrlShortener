from django.db import models

class ShortURL(models.Model):
    original_URL = models.CharField(max_length=2048)                            # Original URL for the shortener. Anything past 2048 characters is a little suspicious so
    short_URL = models.CharField(max_length=512)                                # Backend path to access original URL. Realistically this should never be close to 512
    date_modified = models.DateTimeField(auto_now=True)                         # We want to update the "date_modified" field every time someone generates a URL. That way, we only delete URLS generated after 7 days, but don't waste server space making un-needed URLS

    def save(self, *args, **kwargs):
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return self.original_URL                                                # So that we can see the original URL right away in the admin center
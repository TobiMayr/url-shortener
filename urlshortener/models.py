from django.db import models


class Url(models.Model):
    original_url = models.TextField(primary_key=True)
    short_url = models.TextField(max_length=10)

    class Meta:
        db_table = 'url'
        indexes = [models.Index(fields=['short_url', ]), ]

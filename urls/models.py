import os
from binascii import hexlify

from django.db import models


def generate_id():
    '''Generate an 8-character long hexadecimal ID'''
    possible = hexlify(os.urandom(4)).decode('ascii')
    try:
        Url.objects.get(id=possible)
    except Url.DoesNotExist:
        return possible
    else:
        return generate_id()


class Url(models.Model):
    id = models.TextField(primary_key=True, max_length=8, editable=False, default=generate_id)
    original_url = models.TextField()

    class Meta:
        db_table = 'url'
        indexes = [models.Index(fields=['id', ]), ]

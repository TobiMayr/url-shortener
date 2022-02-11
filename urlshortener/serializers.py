from rest_framework import serializers
from urlshortener.models import Url


class UrlSerializer(serializers.ModelSerializer):
    originalUrl = serializers.CharField(source='original_url')
    shortUrl = serializers.CharField(source='short_url')

    class Meta:
        model = Url
        fields = ['originalUrl', 'shortUrl']

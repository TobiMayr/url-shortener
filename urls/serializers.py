from rest_framework import serializers
from django.conf import settings
from urls.models import Url


class UrlSerializer(serializers.ModelSerializer):

    def get_shortUrl(self, obj):
        return f'{settings.BASE_URL}/{obj.id}'

    originalUrl = serializers.CharField(required=True, source='original_url')
    id = serializers.CharField(required=False, read_only=True)
    shortUrl = serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model = Url
        fields = ['id', 'originalUrl', 'shortUrl']

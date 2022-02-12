from rest_framework import serializers
from urls.models import Url
from urlshortener.settings import BASE_URL


class UrlSerializer(serializers.ModelSerializer):

    def get_shortUrl(self, obj):
        return f'{BASE_URL}/{obj.id}'

    originalUrl = serializers.CharField(required=True, source='original_url')
    id = serializers.CharField(required=False, read_only=True)
    shortUrl = serializers.SerializerMethodField(required=False, read_only=True)

    class Meta:
        model = Url
        fields = ['id', 'originalUrl', 'shortUrl']

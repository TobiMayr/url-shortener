from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from urls import views
from urls.models import Url


class UrlTests(APITestCase):
    # Add one url object to the test database (fixture.json)
    fixtures = ['fixture.json']

    def test_create_new_url(self):
        """
        Ensure we can create a new url object.
        """
        # Clean table before this test
        Url.objects.all().delete()

        url = reverse(views.url_add)
        data = {'originalUrl': 'https://www.google.com/'}
        response = self.client.post(url, data, format='json')
        expected_short_url = f'https://tier.app/{Url.objects.get().id}'
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Url.objects.count(), 1)
        self.assertEqual(response.data['shortUrl'], expected_short_url)

    def test_create_new_url_invalid_original_url(self):
        """
        Ensure invalid original urls throw a 422.
        """
        url = reverse(views.url_add)
        data = {'originalUrl': 'httpswwwgooglecom/'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.content, b'"Enter a valid URL."')

    def test_create_new_url_invalid_body(self):
        """
        Ensure invalid json body throws a 400.
        """
        url = reverse(views.url_add)
        data = {'wrongField': 'https://www.google.com/'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content, b'{"originalUrl":["This field is required."]}')

    def test_get_redirected_valid(self):
        """
        Ensure redirects work for items in the database
        """

        response = self.client.get('/validID0/', format='json')
        self.assertEqual(response.status_code, 302)

    def test_get_redirected_invalid_short_url(self):
        """
        Ensure redirects don't work for items that can't be found in the database
        """
        response = self.client.get('/invalidID/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

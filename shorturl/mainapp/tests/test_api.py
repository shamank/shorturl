from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from mainapp.models import ShortUrls
from mainapp.serializers import ShortUrlSerializer
from django.contrib.auth.models import User

class ShortUrlTestCase(APITestCase):
    def test_get(self):
        user1 = User.objects.create(username='shmk', email='rus@ya.ru')
        url1 = ShortUrls.objects.create(short_url='site1', full_url='https://yandex.ru')
        url2 = ShortUrls.objects.create(short_url='site2', full_url='https://vk.com')
        url3 = ShortUrls.objects.create(short_url='site3', full_url='https://google.com', created_by = user1)
        url = reverse('shorturls-list')
        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(ShortUrlSerializer([url1,  url2, url3], many=True).data, response.data)
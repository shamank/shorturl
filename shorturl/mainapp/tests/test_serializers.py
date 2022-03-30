from django.test import TestCase

from mainapp.serializers import ShortUrlSerializer
from mainapp.models import ShortUrls

class ShortUrlSerializerTestCase(TestCase):
    def test_OK(self):
        url1 = ShortUrls.objects.create(short_url='site1', full_url='https://yandex.ru')
        url2 = ShortUrls.objects.create(short_url='site2', full_url='https://vk.com')
        data = ShortUrlSerializer([url1, url2], many=True).data
        expected_data = [
            {
                'short_url': url1.short_url,
                'full_url': 'https://yandex.ru',
                'created_at': url1.created_at,
                'created_by': None,
                'views': 0
            },
            {
                'short_url': url2.short_url,
                'full_url': url2.full_url,
                'created_at': url2.created_at,
                'created_by': url2.created_by,
                'views': url2.views
            }
        ]

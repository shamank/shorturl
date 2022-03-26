from rest_framework.serializers import ModelSerializer

from .models import ShortUrls

class ShortUrlSerializer(ModelSerializer):
    class Meta:
        model = ShortUrls
        fields = '__all__'

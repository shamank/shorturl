from django.db import models

from django.urls import reverse_lazy

# Create your models here.

class ShortUrls(models.Model):
    short_url = models.SlugField(primary_key=True, verbose_name='Короткая ссылка')
    full_url = models.CharField(max_length=255, verbose_name='Длинная ссылка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    created_by = models.ForeignKey('auth.user', on_delete=models.CASCADE, blank=True, null=True)
    views = models.IntegerField(default=0, verbose_name='Количество переходов')


    def __str__(self):
        return self.short_url

    def get_absolute_url(self):
        return reverse_lazy('info_url', kwargs={'slug': self.pk})

    def to_json(self):
        return {
            'short_url': self.short_url,
            'full_url': self.full_url,
            'created_at': self.created_at,
            'created_by': self.created_by,
            'views': self.views
        }


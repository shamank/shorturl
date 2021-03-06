from django import forms
from .models import ShortUrls


class MakeNewUrl(forms.ModelForm):
    short_url = forms.SlugField(required=False, label='Короткая ссылка', help_text='Оставьте поле пустым, чтобы сгенерировать случайную ссылку', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # full_url = forms.CharField(label='Обычная ссылка', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # created_by = forms.IntegerField()
    #
    # class Meta:
    #     fields = ['short_url', 'full_url',]

    class Meta:
        model = ShortUrls
        fields = ['short_url', 'full_url', ]
        widgets = {
            'short_url': forms.TextInput(attrs={'class': 'form-control'}),
            'full_url': forms.TextInput(attrs={'class': 'form-control', 'rows': 5}),
        }

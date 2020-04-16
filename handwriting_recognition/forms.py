from django import forms
from .models import Images


class IndexForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['img']
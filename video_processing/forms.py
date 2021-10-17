from django import forms
from .models import Videogray, Videocompress


class VideoFormgray(forms.ModelForm):
    class Meta:
        model = Videogray
        fields = ["email", "videofile"]


class VideoFormcompress(forms.ModelForm):
    class Meta:
        model = Videocompress
        fields = ["email", "videofile", "percentage_compression"]

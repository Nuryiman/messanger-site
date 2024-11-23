from django import forms
from .models import CustomUser


class ProfileImage(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['avatar',]

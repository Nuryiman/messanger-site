from django import forms
from .models import *

class ProfileImage(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ['avatar',]

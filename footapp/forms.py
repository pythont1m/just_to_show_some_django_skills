from django import forms
from .models import Players, Clubs

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Players
        fields = '__all__'


class ClubForm(forms.ModelForm):
    class Meta:
        model = Clubs
        fields = '__all__'

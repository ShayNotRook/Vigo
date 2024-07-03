from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'description', 'price', 'category', 'image', 'platform')
    
    
class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=True, label='Search')
# forms.py
from django import forms
from .models import Player

class PlayerSelectionForm(forms.Form):
    player1 = forms.ModelChoiceField(
        queryset=Player.objects.all(), 
        label='Player 1', 
        widget=forms.Select(attrs={'class': 'player-select'})
    )
    player2 = forms.ModelChoiceField(
        queryset=Player.objects.all(), 
        label='Player 2', 
        widget=forms.Select(attrs={'class': 'player-select'})
    )

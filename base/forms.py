# forms.py
from django import forms
from .models import Player

class PlayerSelectionForm(forms.Form):
    player1 = forms.ModelChoiceField(
        queryset=Player.objects.none(),  # 👈 Delay querying until init
        label='Player 1',
        widget=forms.Select(attrs={'class': 'player-select'})
    )
    player2 = forms.ModelChoiceField(
        queryset=Player.objects.none(),
        label='Player 2',
        widget=forms.Select(attrs={'class': 'player-select'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ✅ Safe to query here, DB is ready
        players = Player.objects.all()
        self.fields['player1'].queryset = players
        self.fields['player2'].queryset = players

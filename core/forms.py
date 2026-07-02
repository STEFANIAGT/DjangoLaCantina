from django import forms  # Importa il modulo Django per creare form HTML e gestire input utente
from .models import Wine

class WineForm(forms.ModelForm):
    class Meta: # Classe interna che configura il comportamento del form
        model = Wine # Specifica che il form è basato sul modello Wine
        fields = ['nome', 'cantina', 'regione', 'annata', 'varietà']
# Definisce un form personalizzato (non collegato diretta a un modello)
class VoteForm(forms.Form):
    voto = forms.IntegerField(
        label='Il tuo voto (1-5)',
        min_value=1,
        max_value=5
    )

from django.shortcuts import render   # Per visualizzare template HTML
# Create your views here.
import csv # Modulo Python per leggere/scrivere file CSV
from django.shortcuts import render, redirect, get_object_or_404 # Funzioni utili per gestire le richieste e gli oggetti
from django.views.generic import ListView, DetailView  # Class-based views per liste e dettagli
from .models import Wine
from .forms import VoteForm

# 1) ListView per mostrare tutti i vini  basata su classe
class WineListView(ListView):
    model = Wine
    template_name = 'core/wine_list.html'
    context_object_name = 'object_list'

# 2) DetailView per il dettaglio di un singolo vino
class WineDetailView(DetailView):
    model = Wine
    template_name = 'core/_detail.html'
    context_object_name = 'wine'

# 3) View function per votare un vino
def vota_wine(request, pk):
    wine = get_object_or_404(Wine, pk=pk) # Recupera il vino dal database usando la pk (primary key id)
                                            #Se non lo trova, mostra automaticamente una pagina 404.
    if request.method == 'POST': # se il l’utente ha inviato dati Se è stato inviato un file via POST
                                # spesso tramite un form E salva i dati db


        form = VoteForm(request.POST)  # Crea un'istanza del form con i dati inviati
        if form.is_valid():  # Se i dati sono validi
            voto = form.cleaned_data['voto']  # Estrae il voto dal form
            wine.voto_totale += voto # Aggiunge il voto al totale
            wine.voto_count += 1
            wine.save()
            return redirect('wine_detail', pk=pk) #Dopo aver salvato
                                                        # reindirizza l’utente alla pagina di dettaglio del vino appena votato.
    else:
        form = VoteForm() #Se la richiesta non è POST, mostra un form vuoto
    return render(request, 'core/vote.html', {'wine': wine, 'form': form})

# 4) View function per importazione CSV
#import csv

def import_wines(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        uploaded = request.FILES['csv_file']
        raw_data = uploaded.read() # Legge il contenuto grezzo del file, ottenendo una sequenza di byte.

        try:
            text = raw_data.decode('utf-8') # tenta la codifica
        except UnicodeDecodeError:
            # se fallisce, ripieghiamo su latin-1 (copre Windows-1252)
            text = raw_data.decode('latin-1')

        lines = text.splitlines() #Divide il testo in righe, una per ogni vino
        reader = csv.DictReader(lines) #Usa il modulo csv per leggere ogni riga come dizionario

        for row in reader:
            Wine.objects.create( # Crea un nuovo oggetto Wine
                nome    = row.get('nome','').strip(), # per ottenere il valore corrispondente
                cantina = row.get('cantina','').strip(),
                regione = row.get('regione','').strip(),
                annata  = int(row.get('annata', 0)),
                varietà = row.get('varietà','').strip()
            )

        return redirect('wine_list')

    return render(request, 'core/import.html')


# 5) Class-based view per la classifica Top10
class TopWineView(ListView):
    model = Wine
    template_name = 'core/top_wines.html'
    context_object_name = 'object_list'  # Nome della variabile nel template
    queryset = Wine.objects.all().order_by('-voto_totale')[:10] # ordina in modo decrescente per il voto
                                                                # e non per il voto medio



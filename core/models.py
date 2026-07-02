from django.db import models #Importa le classi base di Django per definire modelli

class Wine(models.Model): # trasferisce le caratteristiche del file models su model
    nome = models.CharField(max_length=200)
    cantina = models.CharField(max_length=200)
    regione = models.CharField(max_length=100)
    annata = annata = models.IntegerField(default=2025)
    varietà = models.CharField(max_length=100, blank=True)
    voto_totale = models.PositiveIntegerField(default=0)
    voto_count = models.PositiveIntegerField(default=0)

    @property # decoratore usa la funzione senza parentesi come fosse un attributo calcolato
    def voto_medio(self):
        if self.voto_count:
            return self.voto_totale / self.voto_count
        return 0# Se non ha voti, restituisce 0

    def __str__(self):# Rappresentazione testuale dell'oggetto
        return f"{self.nome} ({self.annata})"# Utile nell'admin per visualizzare meglio


# Create your models here.

from django.db import models
import datetime
from django.utils import timezone

class MARKA(models.IntegerChoices):
    Volvo = 1
    Scania = 2
    DAF = 3
    Iveco = 4
    MAN = 5
    Mercedes = 6
    Renault = 7

class Ciezarowka(models.Model):
    nazwaCiezarowki = models.CharField(max_length=60, null=True, blank=False)
    nazwaMarki = models.IntegerField(choices=MARKA.choices, default=MARKA.choices[0][0])

    def __str__(self):
        return self.nazwaCiezarowki

class LADUNEK(models.IntegerChoices):
    Explosives = 1
    Gases = 2
    flammableLiquids = 3
    flammableSolids = 4
    Toxic = 5
    corrosiveSubstances = 6

class Zlecenia(models.Model):
    nazwaZlecenia = models.CharField(max_length=60, null=False, blank=False)
    nazwaLadunku = models.IntegerField(choices=LADUNEK.choices, default=LADUNEK.choices[0][0])
    dystans = models.IntegerField(max_length=60, null=False, blank=False)
    czasRealizacji = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nazwaZlecenia

class Kierowca(models.Model):
    imie = models.CharField(max_length=60, null=False, blank=False)
    nazwisko = models.CharField(max_length=60, null=False, blank=False)
    kryteriumLadunek = models.IntegerField(choices=LADUNEK.choices)
    kryteriumDystans = models.IntegerField(max_length=60, null=False, blank=False)
    zlecenia = models.ForeignKey(Zlecenia, null=True, on_delete=models.SET_NULL)
    ciezarowka = models.ForeignKey(Ciezarowka, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ["nazwisko"]


    def __str__(self):
        return self.imie + " " + self.nazwisko




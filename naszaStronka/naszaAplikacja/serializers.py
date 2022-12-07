from rest_framework import serializers
from .models import Kierowca, Ciezarowka, Zlecenia, MARKA, LADUNEK, DYSTANS
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class ZleceniaSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    nazwaZlecenia = serializers.CharField(required=True)
    nazwaLadunku = serializers.ChoiceField(required=True)
    dystans = serializers.CharField(required=True)
    czasRealizacji = serializers.DateTimeField()

    def create(self, validated_data):
        return Zlecenia.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwaZlecenia = validated_data.get('nazwaZlecenia', instance.nazwaZlecenia)
        instance.nazwaLadunku = validated_data.get('nazwaLadunku', instance.nazwaLadunku)
        instance.dystans = validated_data.get('dystans', instance.dystans)
        instance.czasRealizacji = validated_data.get('czasRealizacji', instance.czasRealizacji)
        instance.save()
        return instance

class CiezarowkaSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    nazwaCiezarowki = serializers.CharField(required=True)
    nazwaMarki = serializers.ChoiceField(required=True)

    def create(self, validated_data):
        return Ciezarowka.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwaCiezarowki = validated_data.get('nazwaCiezarowki', instance.nazwaCiezarowki)
        instance.nazwaMarki = validated_data.get('nazwaMarki', instance.nazwaMarki)
        instance.save()
        return instance

class KierowcaSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    kryteriumLadunek = serializers.ChoiceField(choices=LADUNEK)
    kryteriumDystans =serializers.CharField(choices=DYSTANS)
    zlecenia = serializers.PrimaryKeyRelatedField(queryset=Zlecenia.objects.all(), allow_null=True)
    ciezarowka = serializers.PrimaryKeyRelatedField(queryset=Ciezarowka.objects.all(), allow_null=True)

    def create(self, validated_data):
        return Kierowca.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.kryteriumLadunek = validated_data.get('kryteriumLadunek', instance.kryteriumLadunek)
        instance.kryteriumDystans = validated_data.get('kryteriumDystans', instance.kryteriumDystans)
        instance.zlecenia = validated_data.get('zlecenia', instance.zlecenia)
        instance.ciezarowka = validated_data.get('ciezarowka', instance.ciezarowka)

        instance.save()
        return instance
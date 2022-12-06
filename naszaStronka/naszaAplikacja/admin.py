from django.contrib import admin
from .models import Zlecenia, Ciezarowka, Kierowca

class KierowcaAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko', 'zlecenia']

class ZleceniaAdmin(admin.ModelAdmin):
    list_display = ['nazwaZlecenia']
    list_filter = [('nazwaLadunku')]

class CiezarowkaAdmin(admin.ModelAdmin):
    list_display = ['nazwaCiezarowki', 'nazwaMarki']
    list_filter = [('nazwaMarki')]

admin.site.register(Kierowca, KierowcaAdmin)
admin.site.register(Zlecenia, ZleceniaAdmin)
admin.site.register(Ciezarowka, CiezarowkaAdmin)
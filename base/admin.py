from django.contrib import admin
from .models import Player, MalePlayer, FemalePlayer

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_category', 'country', 'gender')

@admin.register(MalePlayer)
class MalePlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_category', 'country')

@admin.register(FemalePlayer)
class FemalePlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_category', 'country')

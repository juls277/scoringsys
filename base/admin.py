from django.contrib import admin
# Register your models here.
from django.conf.urls.static import static

from .models import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_category', 'country')

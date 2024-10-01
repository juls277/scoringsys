from django.apps import AppConfig
from django.contrib import admin
from django.conf.urls.static import static


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    def ready(self):
        from .models import Player

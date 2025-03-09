from django.contrib import admin
from .models import Player, MalePlayer, FemalePlayer, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  # Adds a search bar for categories by name


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'gender')
    filter_horizontal = ('age_categories',)  # Enables multi-selection for categories
    search_fields = ('name', 'country')  # Adds a search bar for players by name and country


@admin.register(MalePlayer)
class MalePlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    exclude = ('gender',)
    filter_horizontal = ('age_categories',)
    search_fields = ('name', 'country')  # Adds a search bar for male players by name and country

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(gender='M')

    def save_model(self, request, obj, form, change):
        obj.gender = 'M'
        super().save_model(request, obj, form, change)


@admin.register(FemalePlayer)
class FemalePlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    exclude = ('gender',)
    filter_horizontal = ('age_categories',)
    search_fields = ('name', 'country')  # Adds a search bar for female players by name and country

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(gender='F')

    def save_model(self, request, obj, form, change):
        obj.gender = 'F'
        super().save_model(request, obj, form, change)

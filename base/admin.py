from django.contrib import admin
from .models import Player, MalePlayer, FemalePlayer, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)  # Adds a search bar for categories by name


class BasePlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')
    filter_horizontal = ('age_categories',)
    exclude = ('gender',)


@admin.register(MalePlayer)
class MalePlayerAdmin(BasePlayerAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(gender='M')

    def save_model(self, request, obj, form, change):
        obj.gender = 'M'
        super().save_model(request, obj, form, change)


@admin.register(FemalePlayer)
class FemalePlayerAdmin(BasePlayerAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(gender='F')

    def save_model(self, request, obj, form, change):
        obj.gender = 'F'
        super().save_model(request, obj, form, change)

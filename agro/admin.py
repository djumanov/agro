from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import FruitType, Fruit


@admin.register(FruitType)
class FruitTypeAdmin(TranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Fruit)
class FruitAdmin(TranslationAdmin):
    list_display = ('fruit_type', 'price')
    search_fields = ('fruit_type__name',)

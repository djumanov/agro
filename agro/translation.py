from modeltranslation.translator import translator, TranslationOptions
from .models import FruitType, Fruit


class FruitTypeTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)  # Ko‘p tillik maydonlar

class FruitTranslationOptions(TranslationOptions):
    fields = ('description',)  # Ko‘p tillik maydonlar

translator.register(FruitType, FruitTypeTranslationOptions)
translator.register(Fruit, FruitTranslationOptions)

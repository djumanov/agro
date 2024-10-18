from modeltranslation.translator import translator, TranslationOptions
from .models import FruitType, Fruit


class FruitTypeTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

class FruitTranslationOptions(TranslationOptions):
    fields = ('description',)

translator.register(FruitType, FruitTypeTranslationOptions)
translator.register(Fruit, FruitTranslationOptions)

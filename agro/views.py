from django.views.generic import TemplateView, DetailView
from .models import FruitType, Fruit


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruit_types'] = FruitType.objects.all()
        return context


class FruitTypeDetailView(DetailView):
    model = FruitType
    template_name = 'fruit_type_detail.html'
    context_object_name = 'fruit_type'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fruits'] = self.object.fruits.all()
        return context

from django.urls import path
from .views import (
    HomeView,
    FruitTypeDetailView,
)


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('fruits/<int:pk>', FruitTypeDetailView.as_view(), name='fruit'),
]

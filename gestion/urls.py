from django.urls import path
from . import views  # Le point seul signifie "dans ce dossier"

urlpatterns = [
    path('', views.liste_taches, name='liste_taches'),
]

from django.shortcuts import render
from .models import Tache

def liste_taches(request):
    taches = Tache.objects.all() # Récupère toutes les tâches de la base
    # Remplace 'gestion/liste.py' par 'gestion/liste.html'
    return render(request, 'gestion/liste.html', {'taches': taches})

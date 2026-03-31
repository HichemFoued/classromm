
from django.db import models

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Tache(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    assigne_a = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    est_terminee = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre
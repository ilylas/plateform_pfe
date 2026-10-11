from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass
    class Role(models.TextChoices):
        ETUDIANT = 'etudiant', 'Étudiant'
        ENCADRANT_PRO = 'encadrant_pro', 'Encadrant professionnel'
        ADMIN = 'admin', 'Administration'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.ETUDIANT)
    entreprise = models.CharField(max_length=100, blank=True)

def __str__(self):
    return f"{self.username} ({self.get_role_display()})"
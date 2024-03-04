from django.db import models

# Create your models here.

class Utilisateur(models.Model):
    nom_util=models.CharField(max_length=50)
    prenom_util=models.CharField(max_length=50)
    pass_util= models.CharField(max_length = 150)
    mail_util=models.EmailField(True)
    
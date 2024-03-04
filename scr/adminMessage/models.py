from django.db import models

# Create your models here.
class AdminMessage(models.Model):
    nom_ad=models.CharField(max_length=50)
    prenom_ad=models.CharField(max_length=50)
    pass_ad= models.CharField(max_length = 150)
from django.db import models

# Create your models here.
class Donor(models.Model) :
    
    name = models.CharField(max_length=80)
    dist = models.CharField(max_length=15)
    cont = models.CharField(max_length=14)
    grp = models.CharField(max_length=5)

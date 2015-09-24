from django.db import models
  
class Bdmap(models.Model):
    url         = models.CharField(max_length=65525, unique=True)
    lnglat      = models.CharField(max_length=30)
    city        = models.CharField(max_length=255)
    price       = models.IntegerField()
    citydomain  = models.CharField(max_length=2)
#    created     = models.DateTimeField('date created')

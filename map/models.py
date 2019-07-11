from django.db import models

  
class Bdmap(models.Model):
    url         = models.CharField(max_length=255, unique=True)
    lng         = models.CharField(max_length=20)
    lat         = models.CharField(max_length=20)
    city        = models.CharField(max_length=255)
    detail      = models.CharField(max_length=255)
    price       = models.IntegerField()
    citydomain  = models.CharField(max_length=2)
    created     = models.DateTimeField('date created')    

    def __str__(self):
        return self.url
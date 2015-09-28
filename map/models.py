from django.db import models
import datetime
  
class Bdmap(models.Model):
    url         = models.CharField(max_length=65525, unique=True)
    lng         = models.CharField(max_length=20)
    lat         = models.CharField(max_length=20)
    city        = models.CharField(max_length=255)
    price       = models.IntegerField()
    citydomain  = models.CharField(max_length=2)
    created     = models.DateTimeField('date created')

    def getRange(self,range):
        now         = datetime.datetime.now()
        locations   = Bdmap.objects.filter(created__gte=datetime(now.year(),now.month()-2,now.date()))
        locations   = Bdmap.objects.filter(lng__gte=range.west && lng__lte=range.east && lat__gte=range.south && lat__lte=range.north)
        return locations
    
    
    
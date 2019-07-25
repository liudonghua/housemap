from django.shortcuts import render
from map.models import Bdmap
import datetime
import json

from django.http import JsonResponse
# Create your views here.

    
def getRange(request):
        now         = datetime.datetime.now()
        range       = request.POST
        
        locations   = []
        locations   = Bdmap.objects.filter(created__gte=datetime.datetime(now.year,now.month-1,now.day,tzinfo=None)
                                    ).filter(lng__gt=range['west']
                                    ).filter(lng__lt=range['east']
                                    ).filter(lat__gt=range['south']
                                    ).filter(lat__lt=range['north']
                                    ).order_by('-created'
                                    ).values('price','lng','lat','url','img','detail')[0:50]

        if locations!=[]:
            #return JsonResponse(data=list(locations),safe=False)
            return JsonResponse(dict(data=list(locations)))
           
        return '[]'
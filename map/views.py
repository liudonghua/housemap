from django.shortcuts import render
from map.models import Bdmap
import datetime
import json

from django.http import JsonResponse
# Create your views here.

    
def getRange(request):
       
        range       = request.POST
        min_price=0 if not range['price'] else int(range['price'])/2
        max_price=10000 if not range['price'] else int(range['price'])*2
        locations   = []
        locations   = Bdmap.objects.filter(created__gte=(datetime.datetime.now()-datetime.timedelta(days=30))
                                    ).filter(lng__gt=range['west']
                                    ).filter(lng__lt=range['east']
                                    ).filter(lat__gt=range['south']
                                    ).filter(lat__lt=range['north']
                                    ).filter(price__gt=min_price
                                    ).filter(price__lt=max_price
                                    ).order_by('-created'
                                    ).values('price','lng','lat','url','img','detail')[0:100]

        if locations!=[]:
            #return JsonResponse(data=list(locations),safe=False)
            return JsonResponse(dict(data=list(locations)))
           
        return '[]'
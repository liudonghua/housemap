from django.db.utils import IntegrityError
from map.models import Bdmap
from scrapy.exceptions import DropItem

class savePipeline(object):
  
    def process_item(self, item, spider):
        geos    = item['lnglat'].split(',')
        geo_lat = geos[1]
        geo_lng = geos[0].lstrip('b')
        maps     = Bdmap(url       = item['url'],
                        lng       = geo_lng,
                        lat       = geo_lat,
                        city      = item['city'],
                        detail    = item['detail'],
                        citydomain= item['citydomain'],
                        price     = item['price'],
                        created   = item['created']
                      )
        try:
            maps.save()
            print("save data !")
        except IntegrityError:
            raise DropItem("Contains duplicate domain: %s" % item['url'])
        return item

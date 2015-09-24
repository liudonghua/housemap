from django.db.utils import IntegrityError
from map.models import Bdmap
from scrapy.exceptions import DropItem

class savePipeline(object):
  
    def process_item(self, item, spider):
#  for item in items:
        map    = Bdmap(url      = item['url'],
                      lnglat    = item['lnglat'],
                      city      = item['city'],
                      citydomain= item['citydomain'],
                      price     = item['price'],
                      )
        try:
            map.save()
            print "save data !"
        except IntegrityError:
          raise DropItem("Contains duplicate domain: %s" % item['url'])
        return item

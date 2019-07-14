from django.db.utils import IntegrityError
from map.models import Bdmap
from scrapy.exceptions import DropItem
import datetime

class savePipeline(object):
  
    def process_item(self, item, spider):
        maps     = Bdmap(url      = item['url'],
                        lng       = item['lng'],
                        lat       = item['lat'],
                        img       = item['img'],
                        detail    = item['detail'],
                        citydomain= item['citydomain'],
                        price     = item['price'],
                        created   = datetime.datetime.now()
                      )
        try:
            maps.save()
            print("save data !")
        except IntegrityError:
            raise DropItem("Contains duplicate domain: %s" % item['url'])
        return item

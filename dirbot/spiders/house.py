from scrapy import Request
from scrapy.selector import Selector
from scrapy.spiders import Spider
from dirbot.items import sitemap
import json

class houseSpider(Spider):
    name = "house"
    allowed_domains = ["ganji.com"]
    start_urls = [
		"http://sz.ganji.com/fang1/",
    ]

    def parse(self, response):
        x         = Selector(response)
        sites = x.xpath('//a[@class="img-box"]/@href').extract()
        
        for site in sites:
            url = "http://sz.ganji.com"+site 
            request=Request(url,callback=self.subparse)
#            request.meta['items'] = items
            yield request
            

    def subparse(self,response):
        item = sitemap() 
    #    open_in_browser(response)
#        items               = response.meta['items']     

        x                   = Selector(response)
        geos                = x.xpath("//div[@id='map_load']/@data-ref").extract()
        if geos!=[]:
            geojson             = json.loads(geos[0],encoding='utf-8');
            item['url']         = response.url.encode('UTF-8')
            item['lnglat']      = geojson['lnglat']
            item['city']        = geojson['city']
            item['citydomain']  = geojson['citydomain']  
            prices              = x.xpath("//li[@class='clearfix']/b[@class='basic-info-price fl']/text()").extract() 
            item['price']       = prices[0]
            created             = x.xpath("//i[@class='f10 pr-5']/text()").extract()
            item['created']     = created[0]
        return item
        
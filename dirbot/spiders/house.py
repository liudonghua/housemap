 # coding: utf-8
from scrapy import Request
from scrapy.selector import Selector
from scrapy.spiders import Spider
from dirbot.items import sitemap
import html2text
import json

class houseSpider(Spider):
    detail = ''
    name = "house"
    allowed_domains = ["ganji.com"]
    start_urls = [
		"http://sz.ganji.com/fang1/",
        "http://gz.ganji.com/fang1/",
        "http://bj.ganji.com/fang1/",
        "http://sh.ganji.com/fang1/",
        "http://wh.ganji.com/fang1/",
        "http://nj.ganji.com/fang1/",
        "http://tj.ganji.com/fang1/",
        "http://hz.ganji.com/fang1/",
        "http://cd.ganji.com/fang1/",
        "http://cq.ganji.com/fang1/",
        "http://cs.ganji.com/fang1/",
        "http://cc.ganji.com/fang1/",
        "http://dl.ganji.com/fang1/",
        "http://dg.ganji.com/fang1/",
        "http://fz.ganji.com/fang1/",
        "http://foshan.ganji.com/fang1/",
        "http://gy.ganji.com/fang1/",
        "http://gl.ganji.com/fang1/",
        "http://huizou.ganji.com/fang1/",
        "http://hf.ganji.com/fang1/",
        "http://hn.ganji.com/fang1/",
        "http://nmg.ganji.com/fang1/",
        "http://jn.ganji.com/fang1/",
        "http://km.ganji.com/fang1/",
        "http://lz.ganji.com/fang1/",
        "http://xz.ganji.com/fang1/",
        "http://nb.ganji.com/fang1/",
        "http://nn.ganji.com/fang1/",
        "http://nc.ganji.com/fang1/",
        "http://qd.ganji.com/fang1/",
        "http://sy.ganji.com/fang1/",
        "http://sjz.ganji.com/fang1/",
        "http://su.ganji.com/fang1/",
        "http://tj.ganji.com/fang1/",
        "http://ty.ganji.com/fang1/",
        "http://wx.ganji.com/fang1/",
        "http://xj.ganji.com/fang1/",
        "http://xa.ganji.com/fang1/",
        "http://xm.ganji.com/fang1/",
        "http://xn.ganji.com/fang1/",
        "http://yc.ganji.com/fang1/",
        "http://zz.ganji.com/fang1/",
        "http://zhuhai.ganji.com/fang1/",
    ]

    def parse(self, response):
        url_base  = response.url.rstrip('/fang1/')
        x         = Selector(response)
#        sites = x.xpath('//a[@class="img-box"]/@href').extract()
        
        for site in  x.css('li.list-img'):
            urls= site.xpath('div[@class="list-mod1"]/a[@class="img-box"]/@href').extract()
            url = url_base+urls[0]
            detail              = site.css('p.list-word span').xpath('text()').extract()
            details             =  [t.encode('utf-8') for t in detail]
            self.detail         = ''.join(details)
            request             = Request(url,callback=self.subparse)
            yield request
            
    def subparse(self,response):
        item = sitemap() 
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
            item['detail']      = self.detail
        return item
        
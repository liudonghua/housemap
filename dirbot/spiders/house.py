 # coding: utf-8
from scrapy import Request
from scrapy.selector import Selector
from scrapy.spiders import Spider
from dirbot.items import sitemap
import html2text
import json
import re


class houseSpider(Spider):
    res =  sitemap()  
    name = "house"
    allowed_domains = ["ganji.com"]
    start_urls = [
		"http://sz.ganji.com/zufang/",
        # "http://gz.ganji.com/fang1/",
        # "http://bj.ganji.com/fang1/",
        # "http://sh.ganji.com/fang1/",
        # "http://wh.ganji.com/fang1/",
        # "http://nj.ganji.com/fang1/",
        # "http://tj.ganji.com/fang1/",
        # "http://hz.ganji.com/fang1/",
        # "http://cd.ganji.com/fang1/",
        # "http://cq.ganji.com/fang1/",
        # "http://cs.ganji.com/fang1/",
        # "http://cc.ganji.com/fang1/",
        # "http://dl.ganji.com/fang1/",
        # "http://dg.ganji.com/fang1/",
        # "http://fz.ganji.com/fang1/",
        # "http://foshan.ganji.com/fang1/",
        # "http://gy.ganji.com/fang1/",
        # "http://gl.ganji.com/fang1/",
        # "http://huizou.ganji.com/fang1/",
        # "http://hf.ganji.com/fang1/",
        # "http://hn.ganji.com/fang1/",
        # "http://nmg.ganji.com/fang1/",
        # "http://jn.ganji.com/fang1/",
        # "http://km.ganji.com/fang1/",
        # "http://lz.ganji.com/fang1/",
        # "http://xz.ganji.com/fang1/",
        # "http://nb.ganji.com/fang1/",
        # "http://nn.ganji.com/fang1/",
        # "http://nc.ganji.com/fang1/",
        # "http://qd.ganji.com/fang1/",
        # "http://sy.ganji.com/fang1/",
        # "http://sjz.ganji.com/fang1/",
        # "http://su.ganji.com/fang1/",
        # "http://tj.ganji.com/fang1/",
        # "http://ty.ganji.com/fang1/",
        # "http://wx.ganji.com/fang1/",
        # "http://xj.ganji.com/fang1/",
        # "http://xa.ganji.com/fang1/",
        # "http://xm.ganji.com/fang1/",
        # "http://xn.ganji.com/fang1/",
        # "http://yc.ganji.com/fang1/",
        # "http://zz.ganji.com/fang1/",
        # "http://zhuhai.ganji.com/fang1/",
    ]

#     def parse(self, response):
#         url_base  = response.url.rstrip('/zufang/')
#         x         = Selector(response)
# #        sites = x.xpath('//a[@class="img-box"]/@href').extract()
        
#         for site in  x.css('li.list-img'):
#             urls= site.xpath('div[@class="list-mod1"]/a[@class="img-box"]/@href').extract()
#             url = url_base+urls[0]
#             detail              = site.css('p.list-word span').xpath('text()').extract()
#             details             =  [t.encode('utf-8') for t in detail]
#             self.detail         = ''.join(details)
#             request             = Request(url,callback=self.subparse)
#             yield request
            
#     def subparse(self,response):
#         item = sitemap() 
#         x                   = Selector(response)
#         geos                = x.xpath("//div[@id='map_load']/@data-ref").extract()
#         if geos!=[]:
#             geojson             = json.loads(geos[0],encoding='utf-8');
#             item['url']         = response.url.encode('UTF-8')
#             item['lnglat']      = geojson['lnglat']
#             item['city']        = geojson['city']
#             item['citydomain']  = geojson['citydomain']  
#             prices              = x.xpath("//li[@class='clearfix']/b[@class='basic-info-price fl']/text()").extract() 
#             item['price']       = prices[0]
#             created             = x.xpath("//i[@class='f10 pr-5']/text()").extract()
#             item['created']     = created[0]
#             item['detail']      = self.detail
#         return item

    def parse(self,response):
        x    = Selector(response)
        items = x.css('#f_mew_list > div.f-main.f-clear.f-w1190 > div.f-main-left.f-fl.f-w980 > div.f-main-list > div > div.f-list-item.ershoufang-list')
         
        for item in items:
            self.res['url']     =    item.xpath('dl/dd[@class="dd-item title"]/a/@href').extract()[0]
            if self.res['url']=='':
                continue
            self.res['img']     =    item.xpath('dl/dt/div/a/img/@src').extract()[0]
            
            self.res['detail']  =    item.xpath('dl/dd[@class="dd-item size"]/text()').extract()[0].encode('UTF-8')
            price               =    item.xpath('dl/dd[@class="dd-item info"]/div[@class="price"]/span/text()').extract()
            if  price[1]!="元/月":
                continue
            self.res['price']   =    price[0]
            yield Request(self.res['url'],callback=self.subparse)
            
    def subparse(self,response):
        x   = Selector(response)
        json4fes     = x.xpath('//script[@type="text/javascript]').extract()
        if json4fes.len()>1:
            coord = re.split('.(d\.d).(d\.d).\'(D)\'.',json4fes[1])
            if coord.len()==3:
                self.res['lat']        = coord[0]
                self.res['lng']        = coord[1]
                self.res['cityDomain'] = coord[2]   
            return self.res
        return []

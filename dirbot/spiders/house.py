 # coding: utf-8
from scrapy import Request
from scrapy.selector import Selector
from scrapy.spiders import Spider
from dirbot.items import sitemap
import html2text
import json
import re
import time


class houseSpider(Spider):
    res =  sitemap()  
    name = "house"
    allowed_domains = ["ganji.com"]
    start_urls = [
		#"http://sz.ganji.com/zufang/",
        "http://gz.ganji.com/zufang/",
        "http://bj.ganji.com/zufang/",
        "http://sh.ganji.com/zufang/",
        "http://wh.ganji.com/zufang/",
        "http://nj.ganji.com/zufang/",
        "http://tj.ganji.com/zufang/",
        "http://hz.ganji.com/zufang/",
        "http://cd.ganji.com/zufang/",
        "http://cq.ganji.com/zufang/",
        "http://cs.ganji.com/zufang/",
        "http://cc.ganji.com/zufang/",
        "http://dl.ganji.com/zufang/",
        "http://dg.ganji.com/zufang/",
        "http://fz.ganji.com/zufang/",
        "http://foshan.ganji.com/zufang/",
        "http://gy.ganji.com/zufang/",
        "http://gl.ganji.com/zufang/",
        "http://huizou.ganji.com/zufang/",
        "http://hf.ganji.com/zufang/",
        "http://hn.ganji.com/zufang/",
        "http://nmg.ganji.com/zufang/",
        "http://jn.ganji.com/zufang/",
        "http://km.ganji.com/zufang/",
        "http://lz.ganji.com/zufang/",
        "http://xz.ganji.com/zufang/",
        "http://nb.ganji.com/zufang/",
        "http://nn.ganji.com/zufang/",
        "http://nc.ganji.com/zufang/",
        "http://qd.ganji.com/zufang/",
        "http://sy.ganji.com/zufang/",
        "http://sjz.ganji.com/zufang/",
        "http://su.ganji.com/zufang/",
        "http://tj.ganji.com/zufang/",
        "http://ty.ganji.com/zufang/",
        "http://wx.ganji.com/zufang/",
        "http://xj.ganji.com/zufang/",
        "http://xa.ganji.com/zufang/",
        "http://xm.ganji.com/zufang/",
        "http://xn.ganji.com/zufang/",
        "http://yc.ganji.com/zufang/",
        "http://zz.ganji.com/zufang/",
        "http://zhuhai.ganji.com/zufang/",
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
        time.sleep(2) 
        for item in items:
            time.sleep(2)
            self.res['url']     =    response.urljoin(item.xpath('dl/dd[@class="dd-item title"]/a/@href').extract()[0])
            if self.res['url']=='':
                continue
            self.res['img']     =    item.xpath('dl/dt/div/a/img/@src').extract()[0]
            self.res['detail']  = ''
            details  =    item.xpath('dl/dd[@class="dd-item size"]/span').extract()
            for detail in details:
                self.res['detail']+=detail    

            price               =    item.xpath('dl/dd[@class="dd-item info"]/div[@class="price"]/span/text()').extract()
            if  price[1]!="元/月":
                continue
            self.res['price']   =    price[0]
            request             =    Request(self.res['url'],callback=self.subparse,meta = {"handle_httpstatus_list":[302,301]})
            yield request

    # def parse_redirect(self,response):
    #     print(''+response.headers.location)
    #     request  =   Request(response.urljoin(response.headers.location),callback=self.subparse)
    #     yield request 

    def subparse(self,response):
        x   = Selector(response)
        json4fes     = x.xpath('//script[@type="text/javascript"]/text()').extract()
        if len(json4fes)>1:
            coords = re.split("\n",json4fes[1])
            for coord in coords:
                lat = re.findall(r'____json4fe.bdLat = \'(\d+\.\d+)\';$',coord)
                if len(lat)>0 and lat[0]!='':
                    self.res['lat'] = lat[0]
                    continue
                lng = re.findall(r'____json4fe.bdLon = \'(\d+\.\d+)\';$',coord)
                if len(lng)>0 and lng[0]!='':
                    self.res['lng'] = lng[0]
                    continue
                cityDomain = re.findall(r'____json4fe.cityDomain = \'(\D+)\';$',coord)
                if len(cityDomain)>0 and cityDomain[0]!='':
                    self.res['citydomain']  = cityDomain[0]
            return self.res        

        return []

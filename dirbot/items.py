from scrapy.item import Item, Field


class sitemap(Item):

    lnglat      = Field()
    city        = Field()
    citydomain  = Field()
    price       = Field()
    url         = Field()
    created     = Field()
    detail      = Field()
from scrapy.item import Item, Field


class sitemap(Item):

    lng         = Field()
    lat         = Field()
    img         = Field()
    citydomain  = Field()
    price       = Field()
    url         = Field()
    created     = Field()
    detail      = Field()
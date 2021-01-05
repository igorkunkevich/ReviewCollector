import scrapy


class ReviewsItem(scrapy.Item):
    brand = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    rating = scrapy.Field()
    body = scrapy.Field()
    answer = scrapy.Field()
    pass

import scrapy
from yandex.items import ReviewsItem


class DanaMallSpider(scrapy.Spider):
    name = 'dana_mall'
    allowed_domains = ['yandex.by']
    start_urls = ['http://yandex.by/maps/org/tts_dana_mall/23881345245/reviews/']

    def parse(self, response, **kwargs):
        count_reviews = len(response.xpath("//div[@class='business-review-view__info']").extract())
        counter = [i for i in range(count_reviews)]
        item = ReviewsItem()
        for review_number in counter:
            item["body"] = response.xpath("//div[@itemprop='reviewBody']//text()").extract()[review_number]
            item["author"] = response.xpath("//span[@itemprop='name']/text()").extract()[review_number]
            item["date"] = response.xpath("//meta[@itemprop='datePublished']/@content").extract()[review_number]
            item["rating"] = len(response.xpath("//div[@class='business-rating-badge-view__stars']").extract()
                                 [review_number].split("span><span"))
            # item["answer"] = response.xpath("//div[@class='cmnt-item__message']//text()").extract()[review_number]
            yield item
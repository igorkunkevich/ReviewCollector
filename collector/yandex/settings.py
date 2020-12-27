
BOT_NAME = 'yandex'

SPIDER_MODULES = ['yandex.spiders']
NEWSPIDER_MODULE = 'yandex.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True


ITEM_PIPELINES = {
    'yandex.pipelines.MongoPipeline': 300,
    'yandex.pipelines.DuplicatesPipeline': 300,
}
MONGO_URI = "mongodb+srv://maedris:igor0906@testingcluster.v7j6l.mongodb.net/reviews"
MONGO_DATABASE = "reviews"


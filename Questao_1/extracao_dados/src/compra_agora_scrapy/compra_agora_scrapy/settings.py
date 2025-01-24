# Scrapy settings for compra_agora_scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "compra_agora_scrapy"

SPIDER_MODULES = ["compra_agora_scrapy.spiders"]
NEWSPIDER_MODULE = "compra_agora_scrapy.spiders"

ITEM_PIPELINES = {'compra_agora_scrapy.pipelines.JsonWriterPipeline': 1,}

ROBOTSTXT_OBEY = True

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

LOG_LEVEL = 'INFO'
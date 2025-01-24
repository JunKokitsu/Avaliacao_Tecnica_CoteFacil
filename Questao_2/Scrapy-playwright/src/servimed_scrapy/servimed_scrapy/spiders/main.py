import argparse
from scrapy.crawler import CrawlerProcess
from orders import  orderSpider

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inicie o orderSpider com um ID de pedido.")
    parser.add_argument("order_id", help="ID do pedido a ser buscado")
    args = parser.parse_args()

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0',
        'DOWNLOAD_HANDLERS': {
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        'TWISTED_REACTOR': "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
        'PLAYWRIGHT_BROWSER_TYPE': "chromium",
        'PLAYWRIGHT_LAUNCH_OPTIONS': {"headless": False},
        'LOG_LEVEL': 'INFO',
    })

    process.crawl(orderSpider, order_id=args.order_id)
    process.start()

from scrapy.crawler import CrawlerProcess
from compra_agora_spider import CompraAgoraSpiderSpider
from scrapy.utils.project import get_project_settings

if __name__ == "__main__":
    # executar o spider
    process = CrawlerProcess(get_project_settings())
    process.crawl(CompraAgoraSpiderSpider)
    process.start()

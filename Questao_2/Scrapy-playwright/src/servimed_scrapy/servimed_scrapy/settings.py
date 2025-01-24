

BOT_NAME = "servimed_scrapy"

SPIDER_MODULES = ["servimed_scrapy.spiders"]
NEWSPIDER_MODULE = "servimed_scrapy.spiders"

ROBOTSTXT_OBEY = True

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


# Enable Playwright
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

PLAYWRIGHT_BROWSER_TYPE = "chromium"  # Pode ser "chromium", "firefox" ou "webkit"
PLAYWRIGHT_LAUNCH_OPTIONS = {"headless": True}  # Define se o navegador será exibido

LOG_LEVEL = 'INFO'
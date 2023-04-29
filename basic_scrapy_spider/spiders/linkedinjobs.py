import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk import ScrapeOpsProxyMiddleware
from scrapeops_scrapy.middleware import ScrapeOpsMiddleware

class LinkedInJobItem(scrapy.Item):
    Application_deadline = scrapy.Field()
    Location = scrapy.Field()
    Employment_form = scrapy.Field()
    Employment_type = scrapy.Field()
    Salary_Range = scrapy.Field()
    Education_level = scrapy.Field()
    Years_of_Experience = scrapy.Field()
    Required_languages = scrapy.Field()
    Markets = scrapy.Field()
    Skills = scrapy.Field()
    Description = scrapy.Field()

class LinkedInSpider(scrapy.Spider):
    name = 'linkedin_spider'
    start_urls = ['https://www.linkedin.com/jobs/search?keywords=Python%20developer&location=United%20States']

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            ScrapeOpsProxyMiddleware: 400,
            ScrapeOpsMiddleware: 800
        },
        'SCRAPEOPS_EMAIL': 'your@email.com',
        'SCRAPEOPS_API_KEY': 'your_scrapeops_api_key',
        'FEED_FORMAT': 'json',
        'FEED_URI': 'linkedin_jobs.json'
    }

    def parse(self, response):
        job_listings = response.xpath('//div[contains(@class, "result-card__contents")]')
        for job in job_listings:
            loader = ItemLoader(item=LinkedInJobItem(), selector=job)
            # Extract and map fields from the job listing's HTML
            # ...

            yield loader.load_item()
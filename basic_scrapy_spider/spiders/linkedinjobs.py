import scrapy

class LinkedinJobSpider(scrapy.Spider):
    name = 'linkedinjobs'
    allowed_domains = ['linkedin.com']
    start_urls = ['https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=Worldwide']

    def parse(self, response):
        # Parse job listings
        for job in response.css('li.job-result-card'):
            yield {
                'title': job.css('h3.job-result-card__title::text').get().strip(),
                'company': job.css('h4.job-result-card__subtitle > a::text').get().strip(),
                'location': job.css('span.job-result-card__location::text').get().strip(),
                'posted': job.css('time.job-result-card__listdate::attr(datetime)').get(),
            }

        # Pagination
        next_page = response.css('a.artdeco-pagination__button--next::attr(href)').get()
        if next_page:
            yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse)
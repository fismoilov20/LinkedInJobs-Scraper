# LinkedIn Scraper

# Getting Started
1. Clone this project: `git clone https://github.com/fismoilov20/LinkedInJobs-Scraper.git`
2. Create a Python Virtual Environment: `python3 -m venv venv`
3. Activate the Python Virtual Environment: `source venv/bin/activate`
4. Install Scrapy using pip: `pip install scrapy`
5. Install Proxy using pip: `pip install scrapeops-scrapy-proxy-sdk`
    Go to `settings.py` add your API key and the following lines:
    ```
    ROBOTSTXT_OBEY = False

    SCRAPEOPS_API_KEY = 'YOUR_API_KEY'

    SCRAPEOPS_PROXY_ENABLED = True

    DOWNLOADER_MIDDLEWARES = {
        'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk. ScrapeOpsScrapyProxySdk': 725,
    }
    ```
 To use the ScrapeOps Proxy you need to first install the monitoring SDK: `pip install scrapeops-scrapy`
 Go to `settings.py`and add the following lines:
 ```
    EXTENSIONS = {
    'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
}
    DOWNLOADER_MIDDLEWARES = {
    ## ScrapeOps Monitor
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    
    ## Proxy Middleware
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}
 ```
 Listing the scrapy projects `scrapy list`
 

 # To Run the Project
 Running the scrapy project: `scrapy crawl linkedinjobs -o output.json`
 The extracted job listings will be stored in a JSON file called linkedin_jobs.json
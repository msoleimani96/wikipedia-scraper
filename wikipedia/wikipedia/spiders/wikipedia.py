import scrapy


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["wikipedia.org"]
    global random_article_url
    random_article_url = "https://en.wikipedia.org/wiki/Special:Random"
    start_urls = [random_article_url for page in range(1000)]

    def parse(self, response):
        title = response.css("span.mw-page-title-main::text").extract_first()

        article = {"url": response.url, "title": title}
        yield article

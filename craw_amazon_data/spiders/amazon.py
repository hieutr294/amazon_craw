from email import header
import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def start_requests(self):
        headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
        urls = [
            f'https://www.amazon.com/s?k={self.k}',
        ]
        for url in urls:
            yield scrapy.Request(url=url,headers=headers, callback=self.parse)

    def parse(self, response):
        title = response.xpath('//div[starts-with(@data-asin,"B")]//span[contains(@class,"a-size-medium a-color-base a-text-normal")]/text()').getall()
        price = response.xpath('//div[starts-with(@data-asin,"B")]//a[contains(@class,"a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")]//span[contains(@class,"a-price")]//span[contains(@class,"a-offscreen")]/text()').getall()
        rating = response.xpath('//div[starts-with(@data-asin,"B")]//div[contains(@class,"a-section a-spacing-none a-spacing-top-micro")]//span[contains(@class,"a-icon-alt")]/text()').getall()
        # for i in raw_title:
        #     if i not in raw_title:
        #         parse_title.append(i)

        self.log(title)
        self.log(price)
        self.log(rating)

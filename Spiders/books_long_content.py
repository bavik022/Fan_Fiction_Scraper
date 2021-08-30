import scrapy
from FanFictionScraper.items import BooksItem
from urllib.parse import urljoin

class BooksSpider(scrapy.Spider):
    name = "books1"
    start_urls = [
        "https://www.fanfiction.net/crossovers/Harry-Potter/224/"
    ]
    HOST_URL = "https://www.fanfiction.net"

    def parse(self, response):
        self.logger.info("Spider initiated!!")

        for ebook in response.xpath('//div[@id="list_output"]/table/tr/td[1]/div[position() <= 1000]'):
            book = BooksItem()
            book['bookTitle'] = ebook.xpath('./a/text()').get()
            book['fictions'] = {}
            book['bookLink'] = urljoin(self.HOST_URL, ebook.xpath('./a/@href').get())
            yield scrapy.Request(book['bookLink'], callback=self.parseChild, meta={'book': book})

    def parseChild(self, response):
        book = response.meta['book']
        # tempInfo = tempInfo.split('-')
        # book["fictions"] = zip(tempTitles, tempAuthors, tempLinks)
        book["fictions"]["title"] =  response.xpath('//a[@class="stitle"]/text()').get()
        book["fictions"]["author"] = response.xpath('//div[contains(@class, "z-list zhover zpointer") and contains(@class ,"z-list zhover zpointer")]/a[position() = 3]/text()').get()
        book["fictions"]["storyLink"] = urljoin(self.HOST_URL, response.xpath('//a[@class="stitle"][1]/@href').get())
        book["fictions"]["otherInfo"] =  response.xpath('string(//div[@class="z-padtop2 xgray"])').get()
        # book["fictions"]["audience"] = tempInfo[0].split(':')[1]
        # book["fictions"]["language"] = tempInfo[1]

        yield scrapy.Request(book["fictions"]["storyLink"], callback=self.parseGrandChild, meta={'book': book})

    def parseGrandChild(self, response):
        book = response.meta['book']
        x = response.xpath('//div[@class="storytext xcontrast_txt nocopy"]/p/text()').getall()
        book["fictions"]["story"] = ','.join(x)

        yield book

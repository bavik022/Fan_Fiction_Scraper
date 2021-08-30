import scrapy
from scrapy import Request
import json
from dicttoxml import dicttoxml


class Books(scrapy.Spider):
    name = 'books'
    start_urls = ['https://www.fanfiction.net/book/']

    def parse(self, response):
        i = 0
        book_list = []
        links = []
        titles = []
        # Get 10 most popular books
        for book in response.xpath("//div[@id='list_output']//a"):
            i = i+1
            if(i > 10):
                break
            title = str(book.xpath('@title').extract()[0])
            link = str(book.xpath('@href').extract()[0])
            book_entry = {'title': title, 'link': link}
            titles.append(title)
            links.append(link)
            book_list.append(book_entry)

        f = open("books.json", "w")
        f.write(json.dumps(book_list))
        f.close()

        xml = dicttoxml(book_list, custom_root="books", attr_type=False)
        f = open("books.xml", "wb")
        f.write(xml)
        f.close()

        for i in range(len(titles)):
            url = links[i]
            #print("URL:", response.urljoin(url))
            yield Request(url=response.urljoin(url), callback=self.reviews, meta={'title': titles[i]})

    def reviews(self, response):
        review_list = {}  # Review Dictionary
        book_title = response.meta['title']
        # List of tags for each element (To allow a JSON dump)
        review_list[book_title] = []
        titles = []
        authors = []
        texts = []
        #print("* Review for :: ", book_title)

        for title in response.xpath('//*[@id="content_wrapper_inner"]/div[position()>3]/a[1]/text()').extract():
            titles.append(title)

        for author in response.xpath('//*[@id="content_wrapper_inner"]/div[position()>3]/a[3]/text()').extract():
            authors.append(author)

        for text in response.xpath('//*[@id="content_wrapper_inner"]/div[position()>3]/div/text()').extract():
            texts.append(text)

        limit = 15
        for i in range(limit):
            review_list[book_title].append({
                'title': titles[i],
                'author': authors[i],
                'text': texts[i]
            })

       # Write JSON
        f = open(book_title+".json", "w")
        f.write(json.dumps(review_list[book_title]))
        f.close()

        # Write XML
        xml = dicttoxml(review_list[book_title],
                        custom_root="".join(book_title.split()), attr_type=False)
        f = open(book_title+".xml", "wb")
        f.write(xml)
        f.close()
        yield review_list

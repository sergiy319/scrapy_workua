import scrapy
from scrapy import Request

from scrapy_workua.items import PeopleItem


class WorkuaSpider(scrapy.Spider):
    name = 'workua'
    allowed_domains = ['work.ua']
    start_urls = [
        'https://www.work.ua/resumes-kharkiv/',
    ]

    site_url = 'https://work.ua'

    def parse(self, response):
        # A loop is created to parse specific data.
        for person in response.css('div.card.resume-link'):
            applicant_name = person.css('div > b::text').get()
            applicant_old = person.css('div > span:nth-child(3)::text').get()
            applicant_position = person.css('h2 > a::text').get()

            people_item = PeopleItem()
            people_item['applicant_name'] = applicant_name.strip()
            people_item['applicant_old'] = applicant_old
            people_item['applicant_position'] = applicant_position.strip()

            # yield people_item

            # A page is created for more detailed information display.
            detail_page_uri = person.css('div.row div a::attr(href)').get()
            detail_page_url = self.site_url + detail_page_uri

            yield Request(detail_page_url, self.parse_detail_page, meta={
                'people_item': people_item,
            })

        # A response is created to go to another search page.
        # next_page_uri = response.css('ul.pagination-small li a::attr(href)').getall() # noqa
        #
        # if next_page_uri:
        #     next_page_url = self.site_url + next_page_uri[-1]
        #
        #     yield Request(next_page_url)

    # A separate method is created to process a detail_page.
    def parse_detail_page(self, response):
        detail_info = response.css('p#addinfo::text').get()

        people_item = response.meta['people_item']
        people_item['detail_info'] = detail_info

        yield people_item

import scrapy


class WorkuaSpider(scrapy.Spider):
    name = 'workua'
    allowed_domains = ['work.ua']
    start_urls = [
        'https://www.work.ua/resumes-kharkiv/',
    ]

    def parse(self, response):
        # A loop is created to parse specific data.
        for person in response.css('div.card.resume-link'):
            applicant_name = person.css('div > b::text').get()
            applicant_old = person.css('div > span:nth-child(3)::text').get()
            applicant_position = person.css('h2 > a::text').get()

            yield {
                "applicant_name": applicant_name,
                "applicant_old": applicant_old,
                "applicant_position": applicant_position,
            }

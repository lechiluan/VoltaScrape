import scrapy


class EnergySpider(scrapy.Spider):
    name = "energy"
    allowed_domains = ["energy.nsw.gov.au"]
    start_urls = ["https://www.energy.nsw.gov.au/households/rebates-grants-and-schemes/find-energy-rebate/"]

    def parse(self, response, **kwargs):
        pass


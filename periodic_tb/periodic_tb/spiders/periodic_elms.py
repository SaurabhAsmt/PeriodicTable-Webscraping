from typing import Iterable
import scrapy
from scrapy import Request
from ..items import PeriodicTbItem
from scrapy.loader import ItemLoader
class PeriodicElmsSpider(scrapy.Spider):
    name = "periodic_elms"
    allowed_domains = ["nih.gov"]
    start_urls = ["https://pubchem.ncbi.nlm.nih.gov/ptable/"]

    def start_requests(self) -> Iterable[Request]:
        yield scrapy.Request('https://pubchem.ncbi.nlm.nih.gov/ptable/',
        meta = dict(playwright = True))

    def parse(self, response):
        for element in response.css("div.ptable div.element"):
            i = ItemLoader(item= PeriodicTbItem(), selector= element)

            i.add_css('symbol','[data-tooltip = "Symbol"]')
            i.add_css('name', '[data-tooltip = "Name"]')
            i.add_css('atomic_number', '[data-tooltip = "Atomic Number"]')
            i.add_css('atomic_mass', '[data-tooltip *= "Atomic Mass"]')
            i.add_css('chemical_group', '[data-tooltip = "Chemical Group Block"]')

            yield i.load_item()


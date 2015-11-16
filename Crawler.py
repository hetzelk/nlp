import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector, Selector

class wikiSpider(CrawlSpider)
	name = 'wikiSpider'
	allowed_domains = ["wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_Page"]
	
    rules = (
    	Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="mw-body-content"//a/@href'))),
    	Rule(SgmlLinkExtractor( allow=("http://en.wikipedia.org/wiki",)),callback="parse_item"),
		)
	
	def parse_item(self, response):
        hxs = HtmlXPathSelector(response)
        #print hxs.select('//h1[@class = "firstHeading"]/span/text()').extract()
        #heading = hxs.select('//h1[@class = "firstHeading"]/span/text()').extract()
		sites = hxs.select('//table[@id="mp-upper"]/tr')
		#sites = hxs.select('//div[@class="mw-body-content"//a/@href')
        items = []
        for site in sites:
            item = WikipediaItem()
            item['title'] = site.select('.//a/text()').extract()
            item['link'] = site.select('.//a/@href').extract()
            item['details'] = site.select('.//p/text()').extract()
            items.append(item)
        return items
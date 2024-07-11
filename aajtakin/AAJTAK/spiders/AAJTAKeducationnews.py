from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import AajtakItem
from scrapy.loader import ItemLoader


class AAJTAKNewsSpider(CrawlSpider):
    
    name = "AAJTAKnews"
    allowed_domains = ["www.aajtak.in"]
    start_urls = [
                "https://www.aajtak.in/education/news",
                "https://www.aajtak.in/topic/weather",
                "https://www.aajtak.in/uttar-pradesh/",
                "https://www.aajtak.in/india/delhi",
                
                ]
    
    rules = (
            Rule(LinkExtractor(allow=(r"india", r"weather", r"education", r"us"), deny=(r"entertainment", r"visualstories", r"video",))),
            # Rule(LinkExtractor(allow=(r"india",))),
            Rule(LinkExtractor(allow=(r"story",)), callback="parse")
            # Rule(LinkExtractor(allow=(r"story",)), callback="parse")

        )

    def parse(self, response):
        """
            examples valid for aajtak.in:
            "title" : response.xpath("//meta[@property='og:title']/@content").extract(),
            "tags" : response.xpath("//meta[@name='keywords']/@content").extract(),
            "locationtags" : response.css("div.tranding-topics-main a::text").getall(),
            "description" : response.xpath("//meta[@property='og:description']/@content").extract(),
            "details" : response.css("p.text-align-justify::text").getall(),
            "time" : response.xpath("/html/body/div[7]/div/div[2]/div[8]/div[1]/div[1]/div[2]/ul/li[3]/text()").getall(),
            "date" : response.xpath("/html/body/div[7]/div/div[2]/div[8]/div[1]/div[1]/div[2]/ul/li[2]/text()").getall(),
            "location" : response.xpath("/html/body/div[7]/div/div[2]/div[8]/div[1]/div[1]/div[2]/ul/li[1]/text()").getall()
            "link" : response.xpath("//link[@rel='canonical']/@href").extract()
        """
        l = ItemLoader(item=AajtakItem(), response=response)
        
        l.add_xpath("title", '//meta[@property="og:title"]/@content')
        l.add_xpath("description", '//meta[@property="og:description"]/@content')
        l.add_css("details", "p.text-align-justify")
        l.add_xpath("time", '/html/body/div[7]/div/div[2]/div[8]/div[1]/div[1]/div[2]/ul/li[3]')
        l.add_xpath("date", 'html/body/div[7]/div/div[2]/div[8]/div[1]/div[1]/div[2]/ul/li[2]')
        l.add_xpath("location", '/html/body/div[7]/div/div[2]/div[8]/div[1]/div[1]/div[2]/ul/li[1]')
        
        # l.add_value("last_updated", "today")  # you can also use literal values
        
        return l.load_item()
    

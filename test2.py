from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy

class TorrentItem(scrapy.Item):
    url = scrapy.Field()

class MininovaSpider(CrawlSpider):

    name = 'mininova'
    allowed_domains = ['baidu.com']
    start_urls = ['https://baike.baidu.com']
    rules = [Rule(LinkExtractor(allow=['/item/.*']), 'parse_torrent')]

    def parse_torrent(self, response):
        torrent = TorrentItem()
        torrent['url'] = response.url
        return torrent

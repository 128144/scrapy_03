# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import RepoItem

class RepoSpider(scrapy.Spider):
    name = 'repo'

    @property
    def start_urls(self):
        url_tmp1 = 'https://github.com/shiyanlou?page={}&tab=repositories'     
        return (url_tmp1.format(i) for i in range(1,5))

    def parse(self, response):
        for course in response.xpath('//*[@id="user-repositories-list"]/ul/li'):
            item =  RepoItem()           
                        
            item['name'] = course.xpath('div[1]/h3/a/text()').re_first('\n\s*(.+)')
            item['update_time'] = course.xpath('div[3]/relative-time/@datetime').extract_first()
            url = 'https://github.com/shiyanlou/' +  item['name']
            request = scrapy.Request(url, callback = self.paser_rep)
            request.meta['item'] = item
            yield request
           
    
    def paser_rep(self, response):
        item = response.meta['item']  
        item['commits'] = response.css('div.repository-content > div.overall-summary > div > div > ul > li:nth-child(1) > a > span').re_first('<span class="num text-emphasized">\n\s*(.+)\n\s*</span>')
        item['branches'] = response.css('div.repository-content > div.overall-summary > div > div > ul > li:nth-child(2) > a > span').re_first('<span class="num text-emphasized">\n\s*(.+)\n\s*</span>')
        item['releases'] = response.css('div.repository-content > div.overall-summary > div > div > ul > li:nth-child(3) > a > span').re_first('<span class="num text-emphasized">\n\s*(.+)\n\s*</span>')
        yield item
        
        




        

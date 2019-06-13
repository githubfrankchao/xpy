# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DushuPipeline(object):
    def process_item(self, item, spider):
        # 将item的信息由日志的INFO记录
        # spider.logger -> logging.LoggerAdapter
        spider.logger.info(item)

        return item

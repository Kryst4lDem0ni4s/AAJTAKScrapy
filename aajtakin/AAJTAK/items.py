# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst, Join
from w3lib.html import remove_tags


def clean_data(value):
    chars_to_remove = ["$", "Item", "#", "/n", "(", ")", "अपडेटेड"]
    for char in chars_to_remove:
        if char in value:
            value = value.replace(char, "")
    return value.strip()

class AajtakItem(scrapy.Item):
    # define the fields for your item here like:
       title = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_data),
        output_processor=TakeFirst()
    
    description = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_data),
        output_processor=TakeFirst()
    )
    details = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_data),
        output_processor=Join()
    )
    time = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_data),
        output_processor=TakeFirst()
    )
    date = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_data),
        output_processor=TakeFirst()
    )
    location = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_data),
        output_processor=TakeFirst()
    )
    

    
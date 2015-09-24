# Scrapy settings for dirbot project
import os
import django


SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.sitemap'
ITEM_PIPELINES = {'dirbot.pipelines.savePipeline': 1}
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36'

def setup_django_env():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gwapp.settings")
      
setup_django_env()


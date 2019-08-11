# Scrapy settings for dirbot project
import os
import django

django.setup()
DOWNLOAD_HANDLERS = {'s3': None,}
SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.sitemap'
ITEM_PIPELINES = {'dirbot.pipelines.savePipeline': 1}
DOWNLOAD_DELAY = 2

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
COOKIES_ENABLED = False

def setup_django_env():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gwapp.settings")
      
setup_django_env()


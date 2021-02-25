# Scrapy settings for scrapy_workua project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_workua'

SPIDER_MODULES = ['scrapy_workua.spiders']
NEWSPIDER_MODULE = 'scrapy_workua.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent # noqa
#USER_AGENT = 'scrapy_workua (+http://www.yourdomain.com)' # noqa

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32 # noqa

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3 # noqa
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16 # noqa
#CONCURRENT_REQUESTS_PER_IP = 16 # noqa

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False # noqa

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False # noqa

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = { # noqa
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', # noqa
#   'Accept-Language': 'en',
#} # noqa

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = { # noqa
#    'scrapy_workua.middlewares.ScrapyWorkuaSpiderMiddleware': 543,
#} # noqa

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = { # noqa
#    'scrapy_workua.middlewares.ScrapyWorkuaDownloaderMiddleware': 543,
#} # noqa

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = { # noqa
#    'scrapy.extensions.telnet.TelnetConsole': None,
#} # noqa

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = { # noqa
#    'scrapy_workua.pipelines.ScrapyWorkuaPipeline': 300,
#} # noqa

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True # noqa
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5 # noqa
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60 # noqa
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0 # noqa
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False # noqa

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings # noqa
#HTTPCACHE_ENABLED = True # noqa
#HTTPCACHE_EXPIRATION_SECS = 0 # noqa
#HTTPCACHE_DIR = 'httpcache' # noqa
#HTTPCACHE_IGNORE_HTTP_CODES = [] # noqa
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage' # noqa

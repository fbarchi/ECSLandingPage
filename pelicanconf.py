AUTHOR = 'Francesco Barchi'
SITEURL = ''
SITENAME = 'ECS Group'
SITETITLE = "ECS Group"
SITESUBTITLE = "Extreme Computing Systems"
SITEDESCRIPTION = "ECS Research Group"
SITELOGO = SITEURL + "/images/logo.png"
FAVICON = SITEURL + "/images/favicon.ico"
#BROWSER_COLOR = "#333"
ROBOTS = "index, follow"
CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}
COPYRIGHT_YEAR = 2023
PATH = 'content'
TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'en'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
# Blogroll
LINKS = (
    ('The research group', 'index.html'),
    ('Blog', 'blog.html'),
    ('---', '#'),
    ('unibo.it', 'https://www.unibo.it/'),
    ('dei.unibo.it', 'https://dei.unibo.it/it'),
    
    #('GROUP', 'https://dei.unibo.it/it/ricerca/gruppi-di-ricerca/programmazione-ottimizzazione-eco-sistemi-cyber-fisici'),
)
# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)
DEFAULT_PAGINATION = 10
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'images',
]
PYGMENTS_RST_OPTIONS = {
    'linenos': 'table'
}
INDEX_SAVE_AS = 'blog.html'

# https://github.com/alexandrevicenzi/Flex/tree/e63fdae267319fdfb5a0788fe2de9e75ce063569
# THEME = "Flex"
# THEME = "../pelican-themes/Flex"
THEME = "./themes/Flex"

# https://github.com/pelican-plugins/render-math
MATH_JAX = {'responsive':True,}

# https://github.com/pelican-plugins/minify
CSS_MIN = True
HTML_MIN = True
INLINE_CSS_MIN = True
INLINE_JS_MIN = True
AUTHOR = "Foo Bar"
SITEURL = "http://yoursite.com"
SITENAME = "Foo Bar's Blog"
SITETITLE = "Foo Bar"
SITESUBTITLE = "Web Developer"
SITEDESCRIPTION = "Foo Bar's Thoughts and Writings"
SITELOGO = SITEURL + "/images/profile.png"
FAVICON = SITEURL + "/images/favicon.ico"

BROWSER_COLOR = "#333"
ROBOTS = "index, follow"

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike",
    "version": "4.0",
    "slug": "by-sa"
}

COPYRIGHT_YEAR = 2020

STATIC_PATHS = ["extra/custom.css"]

EXTRA_PATH_METADATA = {
    "extra/custom.css": {"path": "static/custom.css"},
}

CUSTOM_CSS = "static/custom.css"

MAIN_MENU = True

ADD_THIS_ID = "ra-77hh6723hhjd"
DISQUS_SITENAME = "yoursite"
GOOGLE_ANALYTICS = "UA-1234-5678"
GOOGLE_TAG_MANAGER = "GTM-ABCDEF"

# Enable i18n plugin.
PLUGINS = ["i18n_subsites"]
# Enable Jinja2 i18n extension used to parse translations.
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# Translate to German.
DEFAULT_LANG = "de"
OG_LOCALE = "de_DE"
LOCALE = "de_DE"

# Default theme language.
I18N_TEMPLATES_LANG = "en"

# Pelican-search Configuration
STORK_INPUT_OPTIONS = {"stemming": "German", "url_prefix": SITEURL}
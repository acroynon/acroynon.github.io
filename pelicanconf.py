AUTHOR = 'acroynon'
SITENAME = "acroynon's devlog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Navbar
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    ('HOME', '/'),
    ('ABOUT', '/pages/about.html')
)

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/acroynon'),
    ('Twitter', '#'),
    ('Itch.io', '#')
)

# Blogroll
# LINKS = (
#     ('Github', 'https://github.com/acroynon'),
# )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
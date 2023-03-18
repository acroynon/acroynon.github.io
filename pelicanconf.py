AUTHOR = 'acroynon'
SITENAME = "acroynon's devlog"
SITEURL = 'https://acroynon.com'

PATH = 'content'

THEME = 'notmyidea'

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
    ('BLOG', '/'),
    ('ABOUT', '/pages/about.html')
)

# Social widget
SOCIAL = (
    ('Itch.io', 'https://acroynon.itch.io'),
    ('Github', 'https://github.com/acroynon'),
    ('Twitter', 'https://twitter.com/acroynon'),
    ('YouTube', 'https://youtube.com')
)

# Blogroll
# LINKS = (
#     ('Github', 'https://github.com/acroynon'),
# )

DEFAULT_PAGINATION = 10

PLUGINS = [
    'minchin.pelican.plugins.nojekyll'
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
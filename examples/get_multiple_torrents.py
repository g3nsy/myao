import requests
from myao.sites import NyaaSite
from myao.urls import Formatter
from myao.parameters import Category, Subcategory, Sorting, Order
from myao.extractors import get_multiple_torrents, Parser


formatter = Formatter(
    site=NyaaSite.NYAA_SI,
    query='Lain',
    category=Category.ANIME,
    subcategory=Subcategory.ENGLISH_TRANSLATED,
    sorting=Sorting.SEEDERS,
    order=Order.DESCENDANT,
    rss=False
)

# formatter = Formatter()
# formatter.site = NyaaSite.NYAA_SI
# formatter.query = 'Lain'
# formatter.category = Category.ANIME
# formatter.subcategory = Subcategory.ENGLISH_TRANSLATED
# formatter.sorting = Sorting.SEEDERS
# formatter.order = Order.DESCENDANT

url = formatter.format()

response = requests.get(url)
response.raise_for_status()

torrents = get_multiple_torrents(response.content, Parser.HTML)

for torrent in torrents:
    print()
    print(torrent)

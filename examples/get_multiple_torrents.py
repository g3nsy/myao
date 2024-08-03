import requests
from myao.sites import NyaaSite
from myao.urls import Formatter
from myao.parameters import Category, Subcategory, Sorting, Order
from myao.extractors import get_multiple_torrents


formatter = Formatter()
formatter.site = NyaaSite.NYAA_SI
formatter.query = 'Lain'
formatter.category = Category.ANIME
formatter.subcategory = Subcategory.ENGLISH_TRANSLATED
formatter.sorting = Sorting.SEEDERS
formatter.order = Order.DESCENDANT

url = formatter.format()

response = requests.get(url)
response.raise_for_status()

torrents = get_multiple_torrents(response.content)

for torrent in torrents:
    print()
    print(torrent)

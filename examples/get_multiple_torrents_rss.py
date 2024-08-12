import os, sys, requests


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from myao.urls import format_url
from myao.extractors import get_multiple_torrents_rss
from myao.sites import NyaaSite


url = format_url(
    query='Death Note',
    site=NyaaSite.NYAA_SI,
    rss=True
)

response = requests.get(url)
response.raise_for_status()

torrents = get_multiple_torrents_rss(response.content)

for torrent in torrents:
    print()
    print(torrent)

import os, sys, requests


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from myao.sites import SukebeiSite
from myao.extractors import get_view
from myao.urls import get_single_torrent_url


url = get_single_torrent_url(code=4152019, site=SukebeiSite.SUKEBEI_NYAA)

response = requests.get(url)
response.raise_for_status()

view = get_view(response.content)

print(view.torrent)
print(view.description)
for comment in view.comments:
    print(view.comments)

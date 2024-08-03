import requests
from myao.extractors import get_comments, Parser
from myao.sites import SukebeiSite
from myao.urls import get_single_torrent_url


code = 3332571
url = get_single_torrent_url(code, site=SukebeiSite.SKB_NYAA_HACGN_EU)

response = requests.get(url)
response.raise_for_status()

comments = get_comments(response.content, parser=Parser.HTML5LIB)

for comment in comments:
    print()
    print(comment)

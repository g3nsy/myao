import os, sys, requests


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from myao.sites import SukebeiSite
from myao.urls import get_single_torrent_url
from myao.extractors import get_description, Parser


code = 4152016
url = get_single_torrent_url(code, site=SukebeiSite.SUKEBEI_NYAA)

response = requests.get(url)
response.raise_for_status()

description = get_description(response.content, parser=Parser.LXML)

print(description)

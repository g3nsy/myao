import requests
from myao.sites import SukebeiSite
from myao.urls import get_single_torrent_url
from myao.extractors import get_description


code = 4152016
url = get_single_torrent_url(code, site=SukebeiSite.SUKEBEI_NYAA)

response = requests.get(url)
response.raise_for_status()

description = get_description(response.content)

print(description)

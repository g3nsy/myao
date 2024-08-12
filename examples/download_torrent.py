import os, sys, requests


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from myao.urls import get_download_torrent_url


code = 964646
url = get_download_torrent_url(code)

response = requests.get(url)
response.raise_for_status()

with open(f'{code}.torrent', 'wb') as f:
    f.write(response.content)

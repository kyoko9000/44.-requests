
# open('favicon.ico', 'wb').write(r.content)

# import requests
# import shutil
#
# url = 'http://google.com/favicon.ico'
# def DownloadFile(url):
#     local_filename = url.split('/')[-1]
#     r = requests.get(url)
#     with open(local_filename, 'wb') as f:
#         for chunk in r.iter_content(chunk_size=1024):
#             if chunk:  # filter out keep-alive new chunks
#                 f.write(chunk)
#     return


# DownloadFile(url)
import json

import httpx as httpx
import requests
url = 'https://www.fshare.vn/file/FSHAREUSERPR'
#  "user agent": "getlink-8HH7ZT",
# data = {
#             "user_email": "thanhcanh900@gmail.com",
#             "password": "2rtKaA$_uU7*L(Wwa",
#             "app_key": "dMnqMMZMUnN5YpvKENaEhdQQ5jxDqddt",
#         }
data = {
  "user_email": "{{thanhcanh900@gmail.com}}",
  "password": "{{2rtKaA$_uU7*L(Wwa}}",
  "app_key": "{{dMnqMMZMUnN5YpvKENaEhdQQ5jxDqddt}}"
}
# print(json.dumps(data))
login = requests.get("https://doc-0g-68-docs.googleusercontent.com/docs/securesc/thn9ep0lrjhh4rgkrspq7fnamoi8ubt5/htfi2n49sc0gpp9hlfc1orcqblgnd582/1642293600000/18174458302924210561/18174458302924210561/1DRZuIwvnUUXJO1kFpC01KET-viF7vuZ7?e=download&authuser=0&nonce=o97s0ei1u63hs&user=18174458302924210561&hash=ibpgagpvknugo6hap45424g8g7pvcqri")
print(login.status_code)
print(login.content)
# r = requests.get('https://www.fshare.vn/file/FSHAREUSERPR')
# print(r.status_code)
# #
# print(r.url)
# token = r.url.split("=")[-1]
# print(token)

# payload = {"token": token, "url": url}
# r1 = requests.post("https://api.fshare.vn/api/session/download", data=r.url)
#
# print(r1.content)

# if r.status_code == 200:
#    with open(filename, 'wb') as out:
#       for bits in r.iter_content():
#           out.write(bits)
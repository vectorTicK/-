import requests

cookie = {'Cookie': 'bid="Glu75gZ2me4"; ll="108312"; ct=y; ap=1; ps=y; _ga=GA1.2.590784493.1449735509; ue="tk1011@qq.com"; dbcl2="2971742:RhFMWzA22AQ"; ck=2dKr; push_noty_num=0; push_doumail_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1479481020%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DqQGhVvpu8s501wOLb7Q6IJeLWUGPekLwbi6_suc3Z3i%26wd%3D%26eqid%3D8c8d191600065be20000000558298975%22%5D; _pk_id.100001.8cb4=3c8658747b341374.1449735507.16.1479481020.1479460513.; _pk_ses.100001.8cb4=*; __utmt=1; __utma=30149280.590784493.1449735509.1479472835.1479481021.22; __utmb=30149280.2.10.1479481021; __utmc=30149280; __utmz=30149280.1479117082.10.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.297; _vwo_uuid_v2=98ADFA55613AB2D7DB7CD78E26789A4D|aabf27448d55f545c98fb1ac126b6606'}
url = 'http://www.douban.com'
url2 = 'https://www.douban.com/doumail/'
session = requests.session()
# html = requests.get(url, cookies=cookie).text
# ht2 = session.get(url, cookies=cookie).text
# if '说句话' in html:
#     print('success')
# else:
#     print('failed')
#
# if '说句话' in ht2:
#     print('success')
# else:
#     print('failed')
# ht3 = session.get(url2).text
# if '垃圾豆邮' in ht3:
#     print('success')
# else:
#     print('failed')

url3 = 'https://www.zhihu.com/'
cookie2 = {'Cookie': '_za=7739c805-f737-4919-99b0-902ffb8a353f; d_c0="AGDA7RxwDwqPTpuPFVF5WJtYMDCPD73X-Js=|1465614714"; q_c1=ff256e9f762c424ab1c20583b9030260|1478432920000|1449711919000; _zap=ec0aa00a-f9e7-46ad-82c6-55e86e46cd19; l_cap_id="MWY3NjZmMTE0OTIwNDUzNzhkMmZjYjUxYWU4MTJmODY=|1479262476|8a30757f2ec24ec626c34a87187ff16e6e1b10ef"; cap_id="YTJkNjRlMjIyNzk1NDNjNGE2YWQwNjYwOWM0ZDlhNTY=|1479262476|e3f46137e9601b292be2f38430a97dd4bebaeb4e"; login="YjhjZmZmMzMxY2U0NGNhMzgxN2EyYWZiZGZkZmY4YTc=|1479262497|874fba8ae075ca037d0fcecb26868a018915a4dd"; _xsrf=18cd46f7e04114572e1cf6c589d4532c; __utmt=1; a_t="2.0AABASGUYAAAXAAAA8FFXWAAAQEhlGAAAAGDA7RxwDwoXAAAAYQJVTSFOU1gA07m2oe0rVXrE4-ZebU-gHO1CCSYzkaZBwKRIJl4zd-nFVafgJr3Eag=="; z_c0=Mi4wQUFCQVNHVVlBQUFBWU1EdEhIQVBDaGNBQUFCaEFsVk5JVTVUV0FEVHViYWg3U3RWZXNUajVsNXRUNkFjN1VJSkpn|1479525616|6403f21467123d6c4fe7ca586bb569e8c400cfb7; __utma=51854390.804641502.1479281619.1479479036.1479525496.6; __utmb=51854390.4.10.1479525496; __utmc=51854390; __utmz=51854390.1479390432.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.100--|2=registration_date=20110529=1^3=entry_date=20110529=1'}
agent = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
headers = {'Host': 'www.zhihu.com',
            'Referer': 'http://www.zhihu.com',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
ht4 = session.get(url3, cookies=cookie2, headers=headers).text
if '涂坤' in ht4:
    print('success')
else:
    print('failed')
print(ht4)


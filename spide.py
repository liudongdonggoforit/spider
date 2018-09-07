import urllib.error, urllib.request, urllib.parse
import http.cookiejar
import re

LOGIN_URL = ''
#get_url为使用cookie所登陆的网址，该网址必须先登录才可
get_url = ''
values = {'username':'','passwd':''}
postdata = urllib.parse.urlencode(values).encode()
user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36'
headers = {'User-Agent':user_agent, 'Connection':'keep-alive'}
#将cookie保存在本地，并命名为cookie.txt
cookie_filename = 'cookie.txt'
cookie_aff = http.cookiejar.MozillaCookieJar(cookie_filename)
handler = urllib.request.HTTPCookieProcessor(cookie_aff)
opener = urllib.request.build_opener(handler)

request = urllib.request.Request(LOGIN_URL, postdata, headers)
try:
    response = opener.open(request)
except urllib.error.URLError as e:
    print(e.reason)

cookie_aff.save(ignore_discard=True, ignore_expires=True)

# for item in cookie_aff:
#     print('Name ='+ item.name)
#     print('Value ='+ item.value)
#使用cookie登陆get_url
lists = []
for x in range(1,937):
	print(x)
	urlx = ''
	get_request = urllib.request.Request(urlx,headers=headers)
	get_response = opener.open(get_request)
	pattern_mob = re.compile('1[3|4|5|7|8|9]\d{9}')
	result = pattern_mob.findall(get_response.read().decode('GBK'))
	lists.extend(list(set(result)))
f = open('phone.txt','w')
f.write('|'.join(lists))
f.close()
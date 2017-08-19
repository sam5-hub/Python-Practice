import sys
import urllib.request
import urllib.parse

host = 'http://jisuip.market.alicloudapi.com'
path = '/ip/location'
method = 'GET'
appcode = 'ef2ba5dc51da4a04b828953ea8b83851'
querys = 'ip=122.224.186.100'
bodys = {}
url = host + path + '?' + querys

request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
response = urllib.request.urlopen(request)
content = response.read()
if (content):
	print(content)
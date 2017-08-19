# Requests

# 1.支持HTTP连接保持和连接池
# 2.支持使用cookie保持会话
# 3.支持文件上传
# 4.支持自动确定响应内容的编码
# 5.支持国际化的 URL 和 POST 数据自动编码



import requests
import urllib.parse
import re
from lxml import etree

baidu_url = "http://www.baidu.com/"
google_url = 'https://translate.google.co.jp/?hl=zh-CN&tab=wT#zh-CN/en/你是谁'

# 1.最基本的GET请求可以直接用get方法

def get_request_action():
    response = requests.get(google_url)


# response = requests.request("get", "http://www.baidu.com/")


# 2. 添加 headers 和 查询参数

def custom_request():
#    kw = {'wd': '关键字'} //, params=kw
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    # 使用response.text 时，Requests 会基于 HTTP 响应的文本编码自动解码响应内容，大多数 Unicode 字符集都能被无缝地解码。
    
    response = requests.get(google_url, headers=headers, verify=False)
    
    # 查看响应内容，response.text 返回的是Unicode格式的数据
    print(response.text)

    # 查看响应内容，response.content返回的字节流数据
    # 使用response.content 时，返回的是服务器响应数据的原始二进制字节流，可以用来保存图片等二进制文件。
    print(response.content)

    # 查看完整url地址
    print(response.url)  # 'http://www.baidu.com/s?wd=%E9%95%BF%E5%9F%8E'

    # 查看响应头部字符编码
    print(response.encoding)  # 'utf-8'

    # 查看响应码
    print(response.status_code)  # 200 302

# 3.基本POST请求（data参数）

def set_post_request():
    formdata = {
        "type": "AUTO",
        "i": "i love python",
        "doctype": "json",
        "xmlVersion": "1.8",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_ENTER",
        "typoResult": "true"
    }

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    response = requests.post(url, data=formdata, headers=headers)

    # print(response.text)


    # 如果是json文件可以直接显示
    print(response.json())


# 4.代理（proxies参数）

def set_proxies():
    # 根据协议类型，选择不同的代理
    proxies = {
        "http": "http://12.34.56.79:9527",
        "https": "http://12.34.56.79:9527",
    }

    response = requests.get(baidu_url, proxies=proxies)
    print(response.text)


if __name__ == "__main__":
    custom_request()
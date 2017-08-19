# 贴吧数据
import urllib.request
import urllib.parse

# 1. 导入Python SSL处理模块
import ssl
import random

headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}


def tiebaSpider(url, beginPage, endPage):
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50

        filename = "第" + str(page) + "页.html"
        # 组合为完整的 url，并且pn值每次增加50
        fullurl = url + "&pn=" + str(pn)
        # 调用loadPage()发送请求获取HTML页面
        html = loadPage(fullurl, filename)
        # 将获取到的HTML页面写入本地磁盘文件
        writeFile(html, filename)


def loadPage(url, filename):
    print('正在下载' + filename)

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)

    return response.read()


def writeFile(html, filename):
    """
        作用：保存服务器响应文件到本地磁盘文件里
        html: 服务器响应文件
        filename: 本地磁盘文件名
    """
    print("正在存储" + filename)
    with open(filename, 'w') as f:
        f.write(html.decode("utf-8"))
    print("-" * 20)


def inputTieba():
    kw = input("请输入需要爬取的贴吧:")
    # 输入起始页和终止页，str转成int类型
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw": kw})

    # 组合后的url示例：http://tieba.baidu.com/f?kw=lol
    url = url + key
    tiebaSpider(url, beginPage, endPage)


def ssl_request():
    # 2. 表示忽略未经核实的SSL证书认证
    context = ssl._create_unverified_context()
    url = "https://www.12306.cn/mormhweb/"

    request = urllib.request.Request(url, headers=headers)
    # 3. 在urlopen()方法里 指明添加 context 参数
    response = urllib.request.urlopen(request, context=context)
    print(response.read())


def ajax_get_data():
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"
    # 变动的是这两个参数，从start开始往后显示limit个
    formdata = {
        'start': '0',
        'limit': '10'
    }
    data = urllib.parse.urlencode(formdata)
    request = urllib.request.Request(url, data=data, headers=headers)
    response = urllib.request.urlopen(request)
    print(response.read())


def http_handle():
    '''
    但是基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。所以要支持这些功能：

        使用相关的 Handler处理器 来创建特定功能的处理器对象；
        然后通过 urllib.build_opener()方法使用这些处理器对象，创建自定义opener对象；
        使用自定义的opener对象，调用open()方法发送请求。
    '''

    # 构建一个HTTPHandler 处理器对象，支持处理HTTP请求（HTTPS）
    # 会把收包和发包的报头在屏幕上自动打印出来
    http_handler = urllib.request.HTTPHandler(debuglevel=1)
    # 调用build_opener()方法，创建支持处理HTTP请求的opener对象
    opener = urllib.request.build_opener(http_handler)
    # 构建 Request请求
    request = urllib.request.Request("http://www.baidu.com/")

    # 调用自定义opener对象的open()方法，发送request请求
    response = opener.open(request)
    # 获取服务器响应内容
    print(response.read())


def http_proxyHandler():
    # 构建了两个代理Handler，一个有代理IP，一个没有代理IP
    httpproxy_handler = urllib.request.ProxyHandler({"http": "124.88.67.81:80"})
    nullproxy_handler = urllib.request.ProxyHandler({})

    proxySwitch = True  # 定义一个代理开关

    if proxySwitch:
        opener = urllib.request.build_opener(httpproxy_handler)
    else:
        opener = urllib.request.build_opener(nullproxy_handler)

    request = urllib.request.Request("http://www.baidu.com/")

    # 调用自定义opener对象的open()方法，发送request请求
    response = opener.open(request)
    print(response.read())





def cookie_login():
    # 1. 构建一个已经登录过的用户的headers信息
    headers = {
        "Host": "www.renren.com",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",

        # 便于终端阅读，表示不支持压缩文件
        # Accept-Encoding: gzip, deflate, sdch,

        # 重点：这个Cookie是保存了密码无需重复登录的用户的Cookie，这个Cookie里记录了用户名，密码(通常经过RAS加密)
        "Cookie": "anonymid=ixrna3fysufnwv; depovince=GW; _r01_=1; JSESSIONID=abcmaDhEdqIlM7riy5iMv; jebe_key=f6fb270b-d06d-42e6-8b53-e67c3156aa7e%7Cc13c37f53bca9e1e7132d4b58ce00fa3%7C1484060607478%7C1%7C1484060607173; jebecookies=26fb58d1-cbe7-4fc3-a4ad-592233d1b42e|||||; ick_login=1f2b895d-34c7-4a1d-afb7-d84666fad409; _de=BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5; p=99e54330ba9f910b02e6b08058f780479; ap=327550029; first_login_flag=1; ln_uact=mr_mao_hacker@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20140529/1055/h_main_9A3Z_e0c300019f6a195a.jpg; t=214ca9a28f70ca6aa0801404dda4f6789; societyguester=214ca9a28f70ca6aa0801404dda4f6789; id=327550029; xnsid=745033c5; ver=7.0; loginfrom=syshome"
    }
    http_handler = urllib.request.HTTPHandler(debuglevel=1)
    # 调用build_opener()方法，创建支持处理HTTP请求的opener对象
    opener = urllib.request.build_opener(http_handler)
    # 构建 Request请求
    request = urllib.request.Request("http://www.renren.com", headers=headers)
    # 调用自定义opener对象的open()方法，发送request请求
    response = opener.open(request)
    # 获取服务器响应内容
    print(response.read())



if __name__ == "__main__":
    pass

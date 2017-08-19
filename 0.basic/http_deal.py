import urllib.request
import urllib.parse
import http.cookiejar as cookielib
import random


# 随机代理
# 最好用商业代理

def http_random_proxyHandler():
    proxy_list = [
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"},
        {"http": "124.88.67.81:80"}
    ]

    proxy = random.choice(proxy_list)
    httpproxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(httpproxy_handler)
    request = urllib.request.Request("http://www.baidu.com/")
    # 调用自定义opener对象的open()方法，发送request请求
    response = opener.open(request)
    print(response.read())


# 创建cookiejar 保存文件

def build_cookiejar():
    # 构建一个CookieJar对象实例来保存cookie

    cookiejar = cookielib.CookieJar()

    # 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象

    handler = urllib.request.HTTPCookieProcessor(cookiejar)

    # 通过 build_opener() 来构建opener

    opener = urllib.request.build_opener(handler)

    # 4. 以get方法访问页面，访问之后会自动保存cookie到cookiejar中

    opener.open("http://www.baidu.com")

    ## 可以按标准格式将保存的Cookie打印出来

    cookieStr = ""
    for item in cookiejar:
        cookieStr = cookieStr + item.name + "=" + item.value + ";"

    ## 舍去最后一位的分号

    print(cookieStr[:-1])


def save_cookie_to_file():
    # ==================================================#

    # 保存cookie的本地磁盘文件名

    filename = 'cookie.txt'

    # 声明一个MozillaCookieJar(有save实现)对象实例来保存cookie，之后写入文件

    cookiejar = cookielib.MozillaCookieJar(filename=filename)

    # 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象

    cookie_handler = urllib.request.HTTPCookieProcessor(cookiejar)

    # 通过 build_opener() 来构建opener

    opener = urllib.request.build_opener(cookie_handler)

    # 4. 以get方法访问页面，访问之后会自动保存cookie到cookiejar中

    reponse = opener.open("http://www.baidu.com")

    print(reponse)

    # 保存cookie到本地文件

    cookiejar.save()


# 取出cookie

def get_cookie_file():
    filename = 'cookie.txt'

    # 声明一个MozillaCookieJar(有save实现)对象实例来保存cookie，之后写入文件

    cookiejar = cookielib.MozillaCookieJar()

    cookiejar.load(filename)

    # 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象

    cookie_handler = urllib.request.HTTPCookieProcessor(cookiejar)

    # 通过 build_opener() 来构建opener

    opener = urllib.request.build_opener(cookie_handler)

    # 4. 以get方法访问页面，访问之后会自动保存cookie到cookiejar中

    reponse = opener.open("http://www.baidu.com")

    print(reponse)


# 实战：利用cookielib和post登录人人网

def login_renren_cookie():
    # 1. 构建一个CookieJar对象实例来保存cookie
    cookie = cookielib.CookieJar()

    # 2. 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
    cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

    # 3. 通过 build_opener() 来构建opener
    opener = urllib.request.build_opener(cookie_handler)

    # 4. addheaders 接受一个列表，里面每个元素都是一个headers信息的元祖, opener将附带headers信息
    opener.addheaders = [("User-Agent",
                          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]

    # 5. 需要登录的账户和密码
    data = {"email": "mr_mao_hacker@163.com", "password": "alaxxxxxime"}

    # 6. 通过urlencode()转码
    postdata = urllib.parse.urlencode(data)

    # 7. 构建Request请求对象，包含需要发送的用户名和密码
    request = urllib.request.Request("http://www.renren.com/PLogin.do", data=postdata)

    # 8. 通过opener发送这个请求，并获取登录后的Cookie值，
    opener.open(request)

    # 9. opener包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
    response = opener.open("http://www.renren.com/410043129/profile")

    # 10. 打印响应内容
    print(response.read())

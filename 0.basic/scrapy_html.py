from scrapy.selector import Selector
from scrapy.http import HtmlResponse

response = HtmlResponse(url='https://translate.google.co.jp/?hl=zh-CN&tab=wT#zh-CN/en/你是谁', body=body)
sel = Selector(response=response)


print(sel)
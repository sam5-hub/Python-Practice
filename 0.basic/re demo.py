# Pattern 对象的一些常用方法主要有：

# 1.match 方法：从「起始位置」开始查找，一次匹配
# 2.search 方法：从「任何位置」开始查找，一次匹配
# 3.findall 方法：全部匹配，返回列表
# 4.finditer 方法：全部匹配，返回迭代器
# 5.split 方法：分割字符串，返回列表
# 6.sub 方法：替换

import re

zh = r'([\u4E00-\u9FA5]+)'

line = '上海交通大学abc'
regex_str = zh + r"大学"
obj = re.match(regex_str, line)

print(obj)

#贪婪模式与非贪婪模式

divstr = 'aa<div>test1</div>bb<div>test2</div>cc'

#贪婪模式

m = re.search(r'<div>.*</div>',div) #<div>test1</div>bb<div>test2</div>

# 非贪婪模式
m = re.search(r'<div>.*?</div>',div) #<div>test1</div>



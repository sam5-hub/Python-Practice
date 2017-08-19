# 实际上爬虫一共就四个主要步骤：

# 1.明确目标 (要知道你准备在哪个范围或者网站去搜索)
# 2.爬 (将所有的网站的内容全部爬下来)
# 3.取 (去掉对我们没用处的数据)
# 4.处理数据（按照我们想要的方式存储和使用）

import re

pattern1 = re.compile(r'^c(\d*)m$')
line = "c123m"

m = pattern1.match(line)

print(m)




import urllib.request as req  # 这是一个下载器

# 这是一个网址
url = "https://baike.baidu.com/item/%E9%83%AD%E5%BE%B7%E7%BA%B2/175780?fr=aladdin"

# 使用下载器进行下载
response = req.urlopen(url)


# 获取当前的网页信息
html = response.read()

print(html)


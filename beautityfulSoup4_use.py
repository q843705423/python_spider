from bs4 import BeautifulSoup
import urllib.request as req  # 这是一个下载器

# 这是一个网址
url = "https://baike.baidu.com/item/%E9%83%AD%E5%BE%B7%E7%BA%B2/175780?fr=aladdin"

# 使用下载器进行下载
response = req.urlopen(url)

# 获取当前的网页信息
html = response.read()

# 解析的时候有解析方法
soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")

info = soup.find("div", class_="basic-info cmn-clearfix")

# 若find_all 从第一个开始找
# 且顺序不会打乱
# 那么就一定可以做到一一对应
obj = {}
keyList = info.find_all("dt")
valueList = info.find_all("dd")
length = len(keyList)
for i in range(length):
    key = keyList[i].get_text()
    key = key.replace("\n", "")
    value = valueList[i].get_text()
    value = value.replace("\n", "")
    obj[key] = value
print(obj)


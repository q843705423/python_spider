import urllib.request as req
print("Homework 1----------------------------------")
personInformation = {
    "name": "QiQi Chen",
    "sex": "man",
    "age": "18"
}
print(personInformation)

print("Homework 2--------------------------")
names = []
flag = {}
for i in range(10):
    names.append(input())
    flag[names[i][0]] = 1
for key in flag:
    print(key)
print("HomeWork3--------------------------------")
# 1.哪些网站可以访问?
# 可以进行浏览器直接访问的网站，一般爬虫可以访问
# 2.哪些网站不能访问?
# 在国外的被墙的网站,且爬虫没有设置代理的不能访问
# 有反爬虫限制的，没有进行头伪造的不能访问
# 需要登录的，没有模拟登录的爬虫不能访问
# 3.为什么？
# 一般 所见即为所得,
# 爬虫可以爬到的数据的前提是浏览器可以直接访问
# 这样让爬虫模拟用户操作才有可能访问到用户访问的数据
response = req.urlopen("http://www.baidu.com")
text = response.read()
print(text)
response = req.urlopen("https://www.google.com/")
text = response.read()
print(text)


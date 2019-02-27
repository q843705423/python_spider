import ssl
import urllib.request as req  # 这是一个下载器
from bs4 import BeautifulSoup
import re

# 这是一个页面下载器
class HtmlDownloader(object):
    def download(self, url):
        self.url = url
        if url is None:
            return None
        context = ssl._create_unverified_context()
        response = req.urlopen(url, context=context)
        if response.getcode() != 200:
            return None
        return response.read()

# 这是一个页面解析器
class HtmlParser(object):
    def _get_new_url(self, url, soup):
        new_urls = set()
        links = soup.find_all("a", href=re.compile(r"/item"))
        for link in links:
            new_url = link["href"]
            new_full_url = req.urljoin(url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_data(self, url, soup):
        res_data = {"url": url}
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title")
        res_data["title"] = title_node.get_text()
        return res_data

    def parse(self, url, html_content):
        soup = BeautifulSoup(html_content, "html.parser", from_encoding="gbk")
        new_data = self._get_data(url, soup)
        new_url = self._get_new_url(url, soup)
        return new_url, new_data

# 这是一个输出器
class HtmlOutPut(object):

    def __init__(self):
        self.dataList = []

    def collection_data(self, data):
        if data is None:
            return
        self.dataList.append(data)

    def output_html(self):
        file = open("a.html", "w")
        file.write("<html>")
        file.write("<head>")
        file.write("</head>")
        file.write("<body>")
        for item in self.dataList:
            file.write(item["title"])
        file.write("</body>")
        file.write("</html>")


# 这是一个url管理器
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return None
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, new_urls):
        if new_urls is None and len(new_urls) == 0:
            return None
        for url in new_urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url


class SpiderMain(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.manager = UrlManager()
        self.outputer = HtmlOutPut()

    def craw(self, root_url):
        count = 1
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url() and count <= 20:
            url = self.manager.get_new_url()
            html_count = self.downloader.download(url)
            new_url, new_data = self.parser.parse(url, html_count)
            self.manager.add_new_urls(new_url)
            self.outputer.collection_data(new_data)
            count = count + 1
            if count % 5 == 0:
                print("craw %d: %s" % (count, url))

        self.outputer.output_html()


if __name__ == "__main":
    url = "https://baike.baidu.com/item/%E9%83%AD%E5%BE%B7%E7%BA%B2/175780?fr=aladdin"
    spider = SpiderMain()
    spider.craw(url)

"""
htmlDownload = HtmlDownloader()
htmlParse = HtmlParser()
url = "https://baike.baidu.com/item/%E9%83%AD%E5%BE%B7%E7%BA%B2/175780?fr=aladdin"
html = htmlDownload.download(url)   
url, data = htmlParse.parse(url, html)

htmlOutput = HtmlOutPut()
htmlOutput.collection_data(data)
htmlOutput.output_html()
print(url)
print(data)
"""
"""
soup = BeautifulSoup(html, "html.parser", from_encoding="utf-8")
root = soup.find("div", class_="starMovieAndTvplay")
movie_lis = root.find_all("li", class_="listItem")
length = len(movie_lis)
for i in range(length):
    movie_li = movie_lis[i]
    title = movie_li.find("b", class_="title")
    title = title.get_text()
    print(title)
    dtList = movie_li.find_all("dt")
    ddList = movie_li.find_all("dd")
    len2 = len(ddList)
    for j in range(len2):
        print(dtList[j].get_text(), end=":")
        dd = ddList[j]
        a = dd.find("a")
        div = dd.find("div")
        if a is not None:
            print(a.get_text(), end=" ")
        if div is not None:
            print(div.get_text(), end=" ")
        if a is None and div is None:
            print(dd.get_text())
    print("\n-----------")

sets = htmlParse._get_new_url(url=url, soup=root)
print(sets)
"""

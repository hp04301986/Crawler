"""
https://movie.douban.com/subject/26665065/
"""
import requests
import urllib
from bs4 import BeautifulSoup
import time
import random
import csv

class Crawler(object):
    absurl = "https://movie.douban.com/subject/26665065/comments"
    #initUrl = "https://movie.douban.com/subject/26665065/comments?status=P"
    initUrl = "https://movie.douban.com/subject/26665065/comments?start=220&limit=20&sort=new_score&status=P&percent_type="
    def get_url(self, absurl, next_page):
        url = absurl  + next_page
        return url

    def get_cookies(self):
        cookFile = open("cookie.txt", "r")
        cookies = {}
        for line in cookFile.read().split(";"):
            name, value = line.strip().split("=", 1)
            cookies[name] = value
        print(cookies)
        return cookies

    def get_header(self, absurl):
        #refer = "https://movie.douban.com/subject/26665065/comments"
        #=refer = "https://movie.douban.com/subject/26665065"
        userAgent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.38 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.38"
        #language = 'zh-CN,zh;q=0.9'
        #acceptEncode = 'gzip, deflate, br'
        host = 'www.douban.com'
        header = {'Connection':'keep-alive', 'Origin': host, 'Referer':absurl, 'User-Agent':userAgent}
        return header

    def get_html(self, url, headers, cookies):
        proxies = {
            'http': 'http://115.217.253.200:33255',
            'http': 'http://14.117.177.103:808',
            'http': 'http://117.36.103.170:8118',
            'http': 'http://113.128.11.32:25050'
        }
        html = requests.get(url, headers=headers, cookies = cookies, proxies = proxies).text
        #html = requests.get(url, headers=headers).content
        print(html)
        #data = open("data.txt", 'w', encoding='utf-8')
        #data.write(html)
        return html

    def get_data(self, html):
        soup = BeautifulSoup(html, "lxml")
        comment_list = soup.select('.comment > p')
        try:
            next = soup.select('#paginator > a')
            print(next)
            #豆瓣反爬虫，有时候爬出来首页和前页居然是<span>，不是<a>，所以这么写
            if(len(next) == 3) or (len(next == 1)):
                next_page = next[len(next)-1].get('href')
                print(next_page)
        except:
            print("no next_page")
            next_page = []
        data_notes = soup.select('..comment-time')
        return comment_list, next_page, data_notes

craw = Crawler()
headers = craw.get_header(craw.absurl)
cookies = craw.get_cookies()
#第一次取数据
url = craw.initUrl
html = craw.get_html(url, headers, cookies)
comment_list, next_page, date_nodes = craw.get_data(html)
#next_page = "?start=220&limit=20&sort=new_score&status=P&percent_type="
with open('comments.csv', 'w', encoding='GB18030', newline="") as file:
    csvwriter = csv.writer(file, dialect=("excel"))
    for i in range(len(comment_list)):
        comment = comment_list[i].get_text().strip().replace('\n', '')
        date = date_nodes[i].get_text().strip()
        csvwriter.writerow([comment, date])
    while(next_page != []):
        headers = craw.get_header(url)
        url = craw.get_url(craw.absurl, next_page)
        html = craw.get_html(url, headers, cookies)
        comment_list, next_page, date_nodes = craw.get_data(html)
        for i in range(len(comment_list)):
            comment = comment_list[i].get_text().strip().replace('\n', '')
            date = date_nodes[i].get_text().strip()
            csvwriter.writerow([comment, date])
        time.sleep(3 + float(random.randint(1, 100)) / 20)
file.close()


    #while (next_page != []):
        #headers = craw.get_header(url)
        #url = craw.get_url(craw.absurl,next_page);
        #html = craw.get_html(url, headers, cookies)
        #comment_list, next_page, date_nodes = craw.get_data(html)
        #for node in comment_list:
            #comment = node.get_text().replace('\n', '')
            #for date in date_nodes:
                #data = node.get_text.strip()
                #writer.writerrow(date, comment)
        #time.sleep(2 + float(random.randint(1, 100)) / 20)
    #file.close()





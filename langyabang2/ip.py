"""
随机获取ip代理，防止ip被封
"""
from bs4 import BeautifulSoup
import requests
import random

class Ip(object):
    def get_ip_list(self):
        url = 'http://www.xicidaili.com/nn'
        user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        headers = {'User-Agent': user_agent}
        web_data = requests.get(url, headers=headers)
        soup = BeautifulSoup(web_data.text, 'lxml')
        ips = soup.find_all('tr')
        ip_list = []
        for i in range(1, len(ips)):
            ip_info = ips[i]
            tds = ip_info.find_all('td')
            ip_list.append(tds[1].text + ':' + tds[2].text)
        return ip_list

    def get_random_ip(self, ip_lists):
        proxy_list = []
        for ip in ip_lists:
            print(ip)
            proxy_list.append('http://'+ip)
        proxy_ip = random.choice(proxy_list)
        proxies = {'http':proxy_ip}
        print(proxies)
        return proxies

ip = Ip()
ip_list = ip.get_ip_list()
ip.get_random_ip(ip_list)
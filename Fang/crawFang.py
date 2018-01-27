from bs4 import BeautifulSoup
import requests

req = requests.get("http://sh.fang.com/")
req.encoding = "gb18030"
html = req.text
soup = BeautifulSoup(html, "html.parser")

#获取顶层新盘推荐的整个div
div = soup.find("div", attrs={"id": "ti011"})
#获取四个推荐楼盘的div，根据class=“tenrtd”
for house in div.find_all('div', attrs={'class': 'tenrtd'}):
    #根据class=“text1”获取存储楼盘标题的div
    titleDiv = house.find('div', attrs={'class':'text1'})
    title = titleDiv.find('a').text
    #根据class="text2"获取存储楼盘价格的div
    priceDiv = house.find('div',attrs={'class': 'text2'})
    price = priceDiv.find('b').text
    print(title, " ", price)


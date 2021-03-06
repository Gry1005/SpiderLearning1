from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random

base_url = "https://baike.baidu.com"
# 爬过的网页历史
his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]

for i in range(20):

    #每次访问his中的最后一个网址
    url = base_url + his[-1]
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html,"html.parser")

    print(soup.find('h1').get_text(),' url: ',url)
    #观察需要的百科网址的规律
    sub_urls = soup.find_all('a',{'target':'_blank','href':re.compile(r"/item/(%.{2})+/\d+$")})

    #把提取出的网址随机一个放入his中
    if len(sub_urls) !=0:
        his.append(random.sample(sub_urls,1)[0]['href'])
        #print(random.sample(sub_urls,1)[0]['href'])
    else:
        his.pop()





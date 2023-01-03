# 获取2017.10 - 2022.10所有新闻标题及详情页链接

from bs4 import BeautifulSoup
import pandas as pd
import requests

# 收集新闻标题及其对应的链接
title_n_link=[]
index=0

for i in range(54, 55, 1):
    page = requests.get(f"https://oilprice.com/Energy/Oil-Prices/Page-{i}.html")
    soup = BeautifulSoup(page.content, 'html.parser')
    titles_tags = soup.select(".categoryArticle__title")
    links_tags = soup.select(".categoryArticle__content a")

    for j in range(len(titles_tags)):
        title_n_link.append([index, titles_tags[j].contents[0], links_tags[j].attrs.get('href')])
        index=index+1

    print(f"Page {i} completed")

# index, title, link
df=pd.DataFrame(title_n_link, dtype=int)
df.to_excel('Tables/title_n_link1.xls')

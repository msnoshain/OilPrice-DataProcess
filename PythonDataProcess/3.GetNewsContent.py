# 读取title_n_link，获取所有新闻正文与日期，保存在News文件夹下

import datetime
from bs4 import BeautifulSoup
import pandas as pd
import requests
import cardinality

start_date=datetime.datetime.strptime("2017-10-24", "%Y-%m-%d")
data_list=pd.read_excel(r'Tables/title_n_link.xls').values
date_list=[]
index=0

for item in data_list:
    page = requests.get(item[2])
    soup = BeautifulSoup(page.content, 'html.parser')
    content_tags = soup.select("#article-content p")
    date_tags = soup.select(".article_byline")
    
    # 读取正文
    content_text=''
    for child in content_tags:
        content_text=content_text+" "
        content_text=content_text+child.getText()

    content_text=content_text[0:-33]

    # 保存正文
    f = open(f"News/{str(index)}.txt", 'w+', encoding='utf-8')
    f.write(content_text)
    f.close()
       
    print(f'News {index} of {len(data_list)-1} has been written')

    # 读取日期
    for item1 in date_tags:
        date_str=item1.get_text().split('-')[1].strip().split(',')
        year=date_str[1].strip()
        date = datetime.datetime.strptime(date_str[0].strip()+f' {year}', "%b %d %Y")
        date_list.append([index, (date-start_date).days+43032])

    print(f'Date {index} of {len(data_list)-1} has been read')

    index=index+1

#df=pd.DataFrame(date_list, dtype=int)
#df.to_excel('Tables/date.xls')
    
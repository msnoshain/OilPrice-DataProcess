# 词频统计

import pandas as pd

word_dic = {}
word_matrix = []
data_list = pd.read_excel(r'Tables/date.xls').values
text_group = {}

def get_text(path):
    # 读取文件
    f = open(path, 'r', encoding='utf-8')
    txt = f.read()
    f.close()
    
    # 去除噪声
    txt=txt.lower()
    txt_new = ''
    for i in txt:
        if 97 <= ord(i) <= 122 :
            txt_new = txt_new+i
        else:
            txt_new = txt_new+' '

    return txt_new

# 构造单词总集，频次初始化为0
for item in data_list:
    # 读取文件
    txt=get_text(f"News/{str(item[0])}.txt")

    # 写入字典
    words = txt.split()
    for word in words:
        word = word.strip()
        word_dic[word] = 0

    print(f'text {item[0]} has been read')

# 按日期对文章进行分组key: date, value: text_index(list)
for i in range(43020, 44866, 1):
    # 初始化分组
    text_group[i]=[]

for item in data_list:
    # 统计分组
    text_group[item[1]].append(item[0])

#按日期统计词频
for i in range(43020, 44866, 1):
    # 词频置0
    for key in word_dic.keys():
        word_dic[key]=0
    
    # 词频统计
    for index in text_group[i]:
        txt = get_text(f'News/{str(index)}.txt')
        words = txt.split()
        for word in words:
            word = word.strip()
            word_dic[word] = word_dic[word] + 1

    date_list = [i]
    for value in word_dic.values():
        date_list.append(value)   

    word_matrix.append(date_list)

    print(f'date {i} has been counted')

# 获取列表头（单词）
words = ['.date']
for key in word_dic.keys():
    words.append(key)         

# 输出csv
df = pd.DataFrame(word_matrix, dtype=int, columns=words)
df.to_csv('Tables/statistics_unsorted.csv')

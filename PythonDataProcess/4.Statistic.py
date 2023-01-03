# ��Ƶͳ��

import pandas as pd

word_dic = {}
word_matrix = []
data_list = pd.read_excel(r'Tables/date.xls').values
text_group = {}

def get_text(path):
    # ��ȡ�ļ�
    f = open(path, 'r', encoding='utf-8')
    txt = f.read()
    f.close()
    
    # ȥ������
    txt=txt.lower()
    txt_new = ''
    for i in txt:
        if 97 <= ord(i) <= 122 :
            txt_new = txt_new+i
        else:
            txt_new = txt_new+' '

    return txt_new

# ���쵥���ܼ���Ƶ�γ�ʼ��Ϊ0
for item in data_list:
    # ��ȡ�ļ�
    txt=get_text(f"News/{str(item[0])}.txt")

    # д���ֵ�
    words = txt.split()
    for word in words:
        word = word.strip()
        word_dic[word] = 0

    print(f'text {item[0]} has been read')

# �����ڶ����½��з���key: date, value: text_index(list)
for i in range(43020, 44866, 1):
    # ��ʼ������
    text_group[i]=[]

for item in data_list:
    # ͳ�Ʒ���
    text_group[item[1]].append(item[0])

#������ͳ�ƴ�Ƶ
for i in range(43020, 44866, 1):
    # ��Ƶ��0
    for key in word_dic.keys():
        word_dic[key]=0
    
    # ��Ƶͳ��
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

# ��ȡ�б�ͷ�����ʣ�
words = ['.date']
for key in word_dic.keys():
    words.append(key)         

# ���csv
df = pd.DataFrame(word_matrix, dtype=int, columns=words)
df.to_csv('Tables/statistics_unsorted.csv')

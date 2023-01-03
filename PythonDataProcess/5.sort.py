# 单词排序

import operator
import pandas as pd

# 读取列表头
df = pd.read_csv(r'Tables/statistics_unsorted.csv')
columns = df.columns.tolist()

# 对单词冒泡排序
len=len(columns)
for i in range(len-1):
    for j in range(len-i-1):
        if(operator.gt(columns[j], columns[j+1])):
            columns[j], columns[j+1] = columns[j+1], columns[j]

    print(f'trip {i} completed')

# 输出
df[columns].to_csv('Tables/statistics_sorted.csv')
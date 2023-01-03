# ��������

import operator
import pandas as pd

# ��ȡ�б�ͷ
df = pd.read_csv(r'Tables/statistics_unsorted.csv')
columns = df.columns.tolist()

# �Ե���ð������
len=len(columns)
for i in range(len-1):
    for j in range(len-i-1):
        if(operator.gt(columns[j], columns[j+1])):
            columns[j], columns[j+1] = columns[j+1], columns[j]

    print(f'trip {i} completed')

# ���
df[columns].to_csv('Tables/statistics_sorted.csv')
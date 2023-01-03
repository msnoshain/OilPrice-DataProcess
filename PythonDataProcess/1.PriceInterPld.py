# ��ȱʧ�ļ۸����ݽ��в�ֵ

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

# ��ȡexcel
xls = pd.read_excel(r'Tables/raw.xls', dtype=float)
data_list=xls.values

# ����float nan
nan = float('nan')

# ���ڼ���������ߵ�ԭʼ����
x_train=[]
y_train=[]

# ԭ��ȱʧ������
x_nan=[]

# ɸѡѵ������
for item in data_list:
    if not np.isnan(item[1]):
        x_train.append(item[0])
        y_train.append(item[1])

# �����ζ���ʽ�������
predict_func=interp1d(x_train, y_train, kind='cubic')

# ʹ����ϳ����ĺ�������ԭ��ȱʧ������
for item in data_list:
    if np.isnan(item[1]):
        item[1]=predict_func(item[0])

df=pd.DataFrame(data_list, dtype=float)
df.to_excel('Tables/final.xls')
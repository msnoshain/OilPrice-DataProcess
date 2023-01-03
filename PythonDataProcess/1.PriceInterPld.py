# 对缺失的价格数据进行插值

import numpy as np
import pandas as pd
from scipy.interpolate import interp1d

# 读取excel
xls = pd.read_excel(r'Tables/raw.xls', dtype=float)
data_list=xls.values

# 定义float nan
nan = float('nan')

# 用于计算拟合曲线的原始数据
x_train=[]
y_train=[]

# 原本缺失的数据
x_nan=[]

# 筛选训练数据
for item in data_list:
    if not np.isnan(item[1]):
        x_train.append(item[0])
        y_train.append(item[1])

# 用三次多项式进行拟合
predict_func=interp1d(x_train, y_train, kind='cubic')

# 使用拟合出来的函数计算原本缺失的数据
for item in data_list:
    if np.isnan(item[1]):
        item[1]=predict_func(item[0])

df=pd.DataFrame(data_list, dtype=float)
df.to_excel('Tables/final.xls')
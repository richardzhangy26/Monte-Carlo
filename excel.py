from math import sqrt
# 随机数random.random()
from random import random

import numpy as np
import pandas as pd
# 导入norminv
from scipy.stats import norm

# 年化波动率
avolatility = 0.2221
# 年化收益率
ayield = 0.2819
# 原始价格
orignialprice = 4.2284
data = pd.read_csv("./meng.csv")
# 取步长
rate = data['rate']
# 预测净值增长率,数组表示
# predictrate = []
# for i in range(1, 263):
#     predictrate.append(ayield * rate[i] + sqrt(rate[i]) * avolatility * norm.ppf(random()))
# 用ndarray存储预测率
# predict_rate = np.array(predictrate)
# 预测价格数组
# predictprice = []
# 原始价格,变量
# predict_price = 4.2884
predictprice_array_mean0 = []
predictprice_medain = []
for k in range(0, 261):
    for j in range(0, 100):
        predictprice = []
        predictrate = []
        predict_price = 4.2284
        for i in range(1, 263):
            predictrate.append(ayield * rate[i] + sqrt(rate[i]) * avolatility * norm.ppf(random()))
        predict_rate = np.array(predictrate)
        # print(predict_rate)
        for i in predict_rate:
            predict_price = predict_price * (1 + i)
            # 将每个预测价格添加到数组
            predictprice.append(predict_price)
            predictprice_array = np.array(predictprice)
        predictprice_array_mean0.append(predictprice_array[k])
    predictprice_medain.append(np.median(predictprice_array_mean0))
predictprice_medain_array = np.array(predictprice_medain)
print(predictprice_medain_array)

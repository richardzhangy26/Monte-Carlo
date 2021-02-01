from math import sqrt # 随机数random.random()
from random import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd # 导入norminv
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
max_drawdown = []
for j in range(0, 1000):
    predictprice = [4.2284]
    predictrate = []
    drawdown = []
    predict_price = 4.2284
    for i in range(1, 263):
        predictrate.append(ayield * rate[i] + sqrt(rate[i]) * avolatility * norm.ppf(random()))
    predict_rate = np.array(predictrate)
    # print(predict_rate)
    for i in predict_rate:
        predict_price = predict_price * (1 + i)
        # 将每个预测价格添加到数组
        predictprice.append(predict_price)
    for i in range(0, 263):
        draw_down = (predictprice[i] - min(predictprice[i:263])) / predictprice[i]
        drawdown.append(draw_down)
    max_drawdown.append(max(drawdown))
max_drawdown_array = np.array(max_drawdown)
# print(max_drawdown_array.ndim)

x = max_drawdown_array
plt.figure(figsize=(80, 40), dpi=100)
plt.hist(x, 10)
plt.show()

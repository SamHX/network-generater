# Border_length----正方形区域的边长，单位：km
# Node_amount------网络节点的个数
# Alpha------------网络特征参数，Alpha越大，短边相对长边的比例越大
# Beta-------------网络特征参数，Beta越大，边的密度越大
# Sxy--------------用于存储节点的序号，横坐标，纵坐标的矩阵
# Cost-------------用于存储边的费用的邻接矩阵，费用在[2,10]之间随机选取，无边的取无穷大
# Delay------------用于存储边的时延的邻接矩阵，时延等于边的距离除以三分之二光速，无边的取无穷大

import numpy as np


def network_generater(Border_length, Node_amount, Alpha, Beta):
    sxy = np.zeros(3,Node_amount)
    cost = np.zeros(Node_amount,Node_amount)
    delay = np.zeros(Node_amount,Node_amount)
    # 在正方形区域内随机均匀选取Node_amount个节点



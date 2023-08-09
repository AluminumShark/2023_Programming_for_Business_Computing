import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("/Users/liwei/Desktop/商管程設/hw_08/submission_complete.csv")

rows = ["HW1", "HW2", "HW3", "HW4", "HW5", "HW6", "HW7 "]
columns = ["submission_result_score"]


score_list = []

for i in rows:
    df_now = df.loc[df["challenge_title"] == i]
    df_now = df_now["submission_result_score"]
    result = df_now.sum() / len(df_now.index)
    score_list.append(result)



plt.bar(rows, score_list)

plt.yscale("log")

plt.show()


rows_2 = ["HW4（1）給定排程計畫，計算完成時間與總閒置時間", "HW4（2）依據排程演算法計算完成時間與總閒置時間",
           "HW4（3）給定多條生產線，依據排程演算法計算完成時間與總閒置時間", 
           "HW4（4）給定多條生產線，依據排程演算法計算完成時間與總閒置時間"]

score_list2 = []
time_list = []
for i in rows_2:
    df_now = df[df["challenge_title"] == "HW4"]
    df_now = df_now[df_now["problem_title"] == i]
    #df_now = df_now["submission_result_score"]
    df_now = df_now["submission_code_length"]
    result = df_now.sum() / len(df_now.index)
    """
    if i == "HW4（4）給定多條生產線，依據排程演算法計算完成時間與總閒置時間":
        result /= 40
    else:
        result /= 20"""
    score_list2.append(result)
    

rows_2 = ["Q1", "Q2", "Q3", "Q4"]

plt.bar(rows_2, score_list2)

plt.show()
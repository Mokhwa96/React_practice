import pandas as pd
data = pd.read_csv("total.csv")
print(data.columns)
print(data.head())
data = data.drop('Unnamed: 0.1', axis=1)
data = data.drop('Unnamed: 0', axis=1)
data.to_csv("C:/Users/gjaischool/Desktop/My_coding/final_projects/Judi-AI/total1.csv")
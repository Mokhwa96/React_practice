import pandas as pd
from glob import glob

file_names = glob("C:/Users/gjaischool/Desktop/My_coding/final_projects/Judi-AI/merged/*.csv") #폴더 내의 모든 csv파일 목록을 불러온다
print(file_names)
total = pd.DataFrame() #빈 데이터프레임 하나를 생성한다

for file_name in file_names:
    temp = pd.read_csv(file_name, sep=',', encoding='utf-8') #csv파일을 하나씩 열어 임시 데이터프레임으로 생성한다
    total = pd.concat([total, temp]) #전체 데이터프레임에 추가하여 넣는다

print(total.columns)
print(total.head())
total = total.drop('Unnamed: 0.1', axis=1)
total = total.drop('Unnamed: 0', axis=1)
total.to_csv("C:/Users/gjaischool/Desktop/My_coding/final_projects/Judi-AI/total_embedding_done.csv")
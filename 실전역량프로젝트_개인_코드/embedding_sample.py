#과정 1번 : 아래 코드는 판결문의 내용을 가져와 임베딩 처리를 하는 코드입니다.

import openai
from openai.embeddings_utils import get_embedding
import numpy as np
import pandas as pd
import os
os.chdir("C:/Users/gjaischool/Desktop/My_coding/final_projects/Judi-AI")

# api_key 설정
openai.api_key = "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"

# 데이터 불러오기
data = pd.read_csv("data_ruling_utf.csv")

print(data.facts)

# 임베딩 처리후 저장하기
data["embedding"] = data["facts"][0:10].apply(lambda row: get_embedding(row, engine= 'text-embedding-ada-002'))
# 문자열 임베딩 값을 숫자형으로 변환
data["embedding"] = [np.array(eval(x)) for x in data['embedding']]

data.to_csv("data_ruling_embed.csv", encoding = "utf-8", index = False) # CP949로 이용시 오류 발생
print("작업을 완료했습니다.")
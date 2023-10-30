## 데이터 불러오기

from datasets import load_dataset
import pandas as pd
from tqdm import tqdm

# casename classficiation task
data_cn_plus = load_dataset("lbox/lbox_open", "casename_classification_plus")   #31000


# statutes classification task
data_st_plus = load_dataset("lbox/lbox_open", "statute_classification_plus")    #17000

# Legal judgement prediction tasks
data_ljp_criminal = load_dataset("lbox/lbox_open", "ljp_criminal")   #11500
data_ljp_civil = load_dataset("lbox/lbox_open", "ljp_civil")         #5000

# case summarization task
data_summ_plus = load_dataset("lbox/lbox_open", "summarization_plus")

# precedent corpus
data_corpus = load_dataset("lbox/lbox_open", "precedent_corpus")

#-----------------------------------------------------------------------------

#데이터2 -> 상황을 입력받고 판결문을 생성하는 모델을 만들기 위한 데이터


data_ruling = pd.DataFrame()

data_ruling['facts'] = pd.concat([pd.DataFrame(data_ljp_criminal['train']['facts']),
                                  pd.DataFrame(data_ljp_criminal['validation']['facts']),
                                  pd.DataFrame(data_ljp_criminal['test']['facts']),
                                  pd.DataFrame(data_ljp_criminal['test2']['facts']),
                                  pd.DataFrame(data_ljp_civil['train']['facts']),
                                  pd.DataFrame(data_ljp_civil['validation']['facts']),
                                  pd.DataFrame(data_ljp_civil['test']['facts']),
                                  pd.DataFrame(data_ljp_civil['test2']['facts'])], ignore_index=True)


ruling_list = []
for i in range(len(data_ljp_criminal['train']['ruling'])):
    ruling_list.append(data_ljp_criminal['train']['ruling'][i]['text'])
    if i%20 == 0:
        print(i,'/',len(data_ljp_criminal['train']['ruling']))

for i in range(len(data_ljp_criminal['validation']['ruling'])):
    ruling_list.append(data_ljp_criminal['validation']['ruling'][i]['text'])
    if i%20 == 0:
        print(i,'/',len(data_ljp_criminal['validation']['ruling']))

for i in range(len(data_ljp_criminal['test']['ruling'])):
    ruling_list.append(data_ljp_criminal['test']['ruling'][i]['text'])
    if i%20 == 0:
        print(i,'/',len(data_ljp_criminal['test']['ruling']))

for i in range(len(data_ljp_criminal['test2']['ruling'])):
    ruling_list.append(data_ljp_criminal['test2']['ruling'][i]['text'])
    if i%50 ==0:
        print(i,'/',len(data_ljp_criminal['test2']['ruling']))



for i in range(len(data_ljp_civil['train']['ruling'])):
    ruling_list.append(data_ljp_civil['train']['ruling'][i]['text'])
    if i%20 == 0:
        print(i,'/',len(data_ljp_civil['train']['ruling']))

for i in range(len(data_ljp_civil['validation']['ruling'])):
    ruling_list.append(data_ljp_civil['validation']['ruling'][i]['text'])
    if i%20 == 0:
        print(i,'/',len(data_ljp_civil['validation']['ruling']))

for i in range(len(data_ljp_civil['test']['ruling'])):
    ruling_list.append(data_ljp_civil['test']['ruling'][i]['text'])
    if i%20 == 0:
        print(i,'/',len(data_ljp_civil['test']['ruling']))

for i in range(len(data_ljp_civil['test2']['ruling'])):
    ruling_list.append(data_ljp_civil['test2']['ruling'][i]['text'])
    if i%20 == 0:
        print(i,'/',len(data_ljp_civil['test2']['ruling']))



data_ruling['ruling'] = ruling_list

data_ruling['ruling'] = data_ruling['ruling'].str.replace('\n', ' ')
data_ruling['facts'] = data_ruling['facts'].str.replace('\n', ' ')


#데이터 저장
data_ruling.to_csv('C:/Users/gjaischool/Desktop/final_project/data/facts_ruling.csv', mode='w')
'''
Q4.  
두개의 납품처에서 각각 과일과 야채들이 납품되었습니다. 
이를 각각 물 품의 갯수를 나타내는 2개의 딕셔너리로 정리했습니다. 
물품을 정리하기 위해서 2 개의 딕셔너리 객체를 합쳐 출력하는 함수를 제작하세요.

- 중복되는 물품은 합쳐서 표시하세요.
- 각 딕셔너리 데이터의 데이터의 키값을 이용해 중복을 확인해보세요.
'''
from collections import Counter

dict_first = {'사과': 30, '배': 15, '감': 10, '포도': 10}
dict_second = {'사과': 5, '감': 25, '배': 15, '귤': 25}

def merge_dic(dic_first, dict_second):   
    m_counter = dict(Counter(dict_first) + Counter(dict_second))   
    sort_m =dict (sorted(m_counter.items(), key= lambda x: x[0]))
    print(sort_m)

merge_dic(dict_first, dict_second)

        
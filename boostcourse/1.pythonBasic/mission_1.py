'''
Q1.  
 파이썬에서는 리스트 형태의 데이터를 자주 사용합니다. 
 그래서 리스트 를 잘 다루는 것이 중요한데, 다음으로 주어진 리스트 데이터를 다뤄봅시다.😎

- 다양한 데이터를 수집해서 아래와 같은 num_list를 얻었습니다.
- 하지만 우리에게 필요한 데이터는 홀수 데이터입니다.
- 그렇다면 num_list 가 홀수인 데이터만 출력하도록 하는 함수를 작성해보세요.

# 출력
[1, 5, 7, 15, 29]

'''

num_list = [1, 5, 7, 15, 16, 22, 28, 29]

odd_list = []
def get_odd_num(num_list):
    for value in num_list:
        if value % 2 != 0:
            odd_list.append(value)
            
    return odd_list        
    
print(get_odd_num(num_list))
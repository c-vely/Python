'''
Q5. 단어들을 입력받았는데, 자꾸만 숫자들이 섞여들어가는 문제가 있습니다. 
이를 처리하기 위해서 함수에 string을 전달 받은 뒤, 
string 안에서의 숫자를 제거한 후 string만 남은 리스트를 출력하세요. 😎

- string 연산을 이용해서 문자열을 자르는 연산을 사용해보세요.

# 출력 
inputs = "cat32dog16cow5"

string_list = find_string(inputs)
print(string_list)

>>> ["cat", "dog", "cow"]

'''
import re

def find_string(input):
    newStr = re.sub(r'[0-9]+', ' ', input)
    str_list = newStr.split()
    return str_list
   
   
inputs = input("입력하세요 : ")

string_list = find_string(inputs)
print(string_list)    

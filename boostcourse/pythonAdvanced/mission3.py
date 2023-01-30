# Q3
'''
 이번 시험 결과에 대한 데이터를 학과 사무실에서 CSV파일로 전달해줬습니다. 
 우리는 이 파일을 이용해서 데이터 처리를 진행해야 합니다. 
 
 1. 파일 입출력을 이용해 파일 데이터를 리스트로 만들어보세요.


- 파일 입출력에 사용하는 open 함수를 이용해 CSV 파일 내부의 데이터를 읽어보세요

 **CSV파일은 아래 첨부되어있습니다. 
 
 
------------------------

# 파일의 경로를 file_path로 설정
# ex) file_path = "./data-01-testscore.csv"

def read_file(file_path):
    # TODO
    
# 출력 예시
>>> print(read_file())

[['73', '80', '75', '152'],
 ['93', '88', '93', '185'],
 ['89', '91', '90', '180'],
 ['96', '98', '100', '196'],
 ['73', '66', '70', '142'],
 ['53', '46', '55', '101'],
 ['69', '74', '77', '149'],
 ['47', '56', '60', '115'],
 ['87', '79', '90', '175'],
 ['79', '70', '88', '164'],
 ['69', '70', '73', '141'],
 ['70', '65', '74', '141'],
 ['93', '95', '91', '184'],
 ['79', '80', '73', '152'],
 ['70', '73', '78', '148'],
 ['93', '89', '96', '192'],
 ['78', '75', '68', '147'],
 ['81', '90', '93', '183'],
 ['88', '92', '86', '177'],
 ['78', '83', '77', '159'],
 ['82', '86', '90', '177'],
 ['86', '82', '89', '175'],
 ['78', '83', '85', '175'],
 ['76', '83', '71', '149'],
 ['96', '93', '95', '192']]
 
------------------------
 
'''


'''
# 1) 리스트 안에 값 저장되어 출력 됨  ---> ok
#file_path = "./data-01-test-score.csv"
def read_file():
    with open(".\pythonAdvanced\data-01-test-score.csv", "r") as f:
        contents_list = f.readlines()
    return contents_list
   
print(read_file())

'''


'''
# 2) 리스트에 각각 리스트로 저장 잘 안됨 ㅜㅜ
def read_file(file_path):
    with open(file_path, "r",  encoding="utf8") as f:     
        i = 0
        while True:
            line = f.readline()
            if not line:
                break 
            else :
                print("[" + line.replace("\n", "") + "]")   # ---> 맨 끝에 none 이 왜 나오지?
            i += 1   

file_path = ".\pythonAdvanced\data-01-test-score.csv" 
print(read_file(file_path))  # ---> 여기 이상

'''


'''
# 3) 한 줄씩 리스트로 출력  ---> ok
import csv

def read_file(file_path):
    with open(file_path, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)  #  ---> 왜 맨 마지막에 none이 나오징?

file_path = ".\pythonAdvanced\data-01-test-score.csv"
print(read_file(file_path))

'''




# 4)
from pprint import pprint

def read_file(file_path):
    result = []
    with open (file_path, 'r') as f:
        for row in f.readlines():
            result.append(row.replace('\n', '').split(','))
    return result

file_path = ".\pythonAdvanced\data-01-test-score.csv"
pprint(read_file(file_path))
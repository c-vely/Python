# Q4.
'''
 우리는 방금 CSV 파일을 읽는 함수를 구현해보았습니다. 
 하지만 이를 조금 더 효율적으로 사용하기 위해서 클래스로 구성을 진행하려고 합니다. 
 
 1.방금 구현한 함수를 포함한 클래스를 구현해보세요.

 - merge list를 이용해 리스트 내 데이터의 합을 출력해보세요.
 
 - 데이터를 합치기 전 데이터의 자료형을 변경해보세요.
 

--------------------------------------------------------- 
 
# 파일의 경로를 file_path로 설정
# ex) file_path = "./data-01-test-score.csv"

class ReadCSV():
    def __init_(self, file_path) :
        # TODO

    def read_file(self, #):
        # TODO

    def merge_list(self, #):
        # TODO

# 출력 예시
>>> read_csv = ReadCSV(file_path)
>>> print(read_csv.read_file())
>>> print(read_csv.merge_list())

[[73, 80, 75, 152],
 [93, 88, 93, 185],
 [89, 91, 90, 180],
 [96, 98, 100, 196],
 [73, 66, 70, 142],
 [53, 46, 55, 101],
 [69, 74, 77, 149],
 [47, 56, 60, 115],
 [87, 79, 90, 175],
 [79, 70, 88, 164],
 [69, 70, 73, 141],
 [70, 65, 74, 141],
 [93, 95, 91, 184],
 [79, 80, 73, 152],
 [70, 73, 78, 148],
 [93, 89, 96, 192],
 [78, 75, 68, 147],
 [81, 90, 93, 183],
 [88, 92, 86, 177],
 [78, 83, 77, 159],
 [82, 86, 90, 177],
 [86, 82, 89, 175],
 [78, 83, 85, 175],
 [76, 83, 71, 149],
 [96, 93, 95, 192]]

[380, 459, 450, 490, 351, 255, 369, 278, 431, 401, 353, 350, 463, 384, 369, 470, 368, 447, 443, 397, 435, 432, 421, 379, 476]
--------------------------------------------------------- 

'''


'''
# 1)  ---> ok 

import csv

class ReadCSV():
    def __init__(self, file_path) :
        self.file_path = file_path
        self.sum_list = []

    def read_file(self):
        with open(self.file_path, newline=None) as file:
            score = csv.reader(file)
            self.list_data = list(score)
        return [print(value) for value in self.list_data]

    def merge_list(self):
        for value in self.list_data:
            result = sum(list(map(int, value)))
            self.sum_list.append(result)
        return self.sum_list
            

file_path = ".\pythonAdvanced\data-01-test-score.csv"
read_csv = ReadCSV(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())  # ---> 여기서 리스트 none 왜 찍힘?

'''


# 2)
from pprint import pprint

class ReadCSV():
    def __init__(self, file_path) :
        self.file_path = file_path

    def read_file(self):
        result = []
        with open(self.file_path, 'r') as file:
            for row in file.readlines():
                tmp_list = row.replace('\n', '').split(',')
                result.append(list(map(int, tmp_list)))
        return result

    def merge_list(self):
        result = []
        tmp_list = self.read_file()
        for tmp in tmp_list:
            result.append(sum(tmp))
        return result
            

file_path = ".\pythonAdvanced\data-01-test-score.csv"
read_csv = ReadCSV(file_path)
pprint(read_csv.read_file())
print(read_csv.merge_list())
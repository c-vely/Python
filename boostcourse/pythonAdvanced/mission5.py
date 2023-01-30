# Q5.

'''
이전에 구현한 클래스에서 merge_list의 함수 동작을 변경해야합니다. 
단순합계가 아닌 평균을 구하는 함수로 변경해보세요.


 1. 리스트의 데이터를 다루는 함수를 이용해서 구현해보세요.

 2. 최종 평균을 구한 후 오름차순으로 정렬해주세요.
 
 
-----------------------------------------
 
 class ReadCSV() :
    def __init__ (self, file_path) :
        # TODO

    def read_file(self, #) :
        # TODO

    def merge_list(self, #) :
        # TODO

# 출력 예시
>>> read_csv = ReadCSV( file_path)
>>> print(read_csv.merge_list())

[63.75, 69.5, 87.5, 87.75, 88.25, 92.0, 92.25, 
92.25, 94.75, 95.0, 96.0, 99.25, 100.25, 105.25, 
107.75, 108.0, 108.75, 110.75, 111.75, 112.5, 
114.75, 115.75, 117.5, 119.0, 122.5]

-----------------------------------------

'''


# 1)

import csv
class ReadCSV() :
    def __init__ (self, file_path) :
        self.file_path = file_path
        self.avg_list = []

    def read_file(self):
        result = []
        with open(self.file_path, 'r') as file:
            for row in file.readlines():
                tmp_list = row.replace('\n', '').split(',')
                result.append(list(map(int, tmp_list)))
        return result
    
    def merge_list(self):
        list_data = self.read_file()
        for value in list_data:
            sumValue = sum(list(map(int, value)))
            result = sumValue / len(value)
            self.avg_list.append(result)
            self.avg_list.sort()
        return self.avg_list
    
file_path = ".\pythonAdvanced\data-01-test-score.csv"    
read_csv = ReadCSV(file_path)
print(read_csv.merge_list())
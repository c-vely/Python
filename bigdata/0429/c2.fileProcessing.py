'''
# 파일 생성
f = open('C:/Users/LG\dev/bigdata/0429/babo.txt', 'w')

for i in range (1, 11):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close


# 파일 읽기 1
f = open('C:/Users/LG\dev/bigdata/0429/babo.txt', 'r')

while True:
    line = f.readline()
    if not line: break
    print(line)

f.close()


# 파일 읽기 2
f = open('C:/Users/LG\dev/bigdata/0429/babo.txt', 'r')

lines = f.readlines()
for line in lines:
    line = line.strip() #줄 끝의 줄 바꿈 문자를 제거한다.
    print(line)

f.close()


# csv 생성
import csv

f = open('write.csv', 'w', newline='')
wr = csv.writer(f)

wr.writerow([1, '홍길동', '부산'])
wr.writerow([2, '김복순', '서울'])

f.close()


# csv 읽기
import csv

f = open('write.csv', 'r')
rdr = csv.reader(f)

for line in rdr:
    print(line)

f.close()


# csv 파일 수정 
import csv

f = open('write.csv', 'r')
rdr = csv.reader(f)
lines = []

for line in rdr:
    if line[0] == '림코딩':
        line[1] = '서울'
    lines.append(line)

f = open('example.csv', 'w', newline = '')
wr = csv.writer(f)
wr.writerows(lines)

f.close()


# json
import json

data = {
    "olivia" : {
        "gender": "female",
        "age" : 25,
        "hobby" : ["reading", "music"]
    },
    "Tyler" : {
        "gender": "male",
        "age" : 28,
        "hobby" : ["development", "painting"]
    }
}

file_path = "./test.json"

with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent="\t")


'''
#json 라이브러리 포함시키기
import json

#json 문자열 데이터
employee_string = '{"first_name": "Michael", "last_name": "Rodgers", "department": "Marketing"}'

#type() 함수로 자료형 확인하기
print(type(employee_string))
print(employee_string)

#문자열을 객체로 변환하기
json_object = json.loads(employee_string)

#새로운 자료형 확인하기
print(type(json_object))
print(json_object)

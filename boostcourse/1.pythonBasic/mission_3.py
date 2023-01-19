'''
Q3. 이번 학기의 중간고사, 기말고사 점수가 발표되었습니다. 
각 학생들의 점수가 튜플 형태로 저장되어 있고, 이를 포함한 리스트가 있습니다. 
이를 이용 해 각 학생들의 평균 점수를 출력하는 함수를 제작하세요. 😎

- 리스트와 반복문을 사용해 데이터를 불러오세요.
- 이를 이용해 각 학생별 평균을 구해보세요

# 출력
1 번, 평균 : 100.0
2 번, 평균 : 92.5
3 번, 평균 : 57.5
4 번, 평균 : 77.5
5 번, 평균 : 70.0

'''


score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

sum_list = []
def get_avg(score):
    for value in score:
        sum = 0
        for j in value:
            sum += j
        sum_list.append(sum)
    for i in range(len(sum_list)):     
        print(f'{i+1} 번, 평균 : {sum_list[i] / 2:.1f}')

get_avg(score)
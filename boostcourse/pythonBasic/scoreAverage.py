# 사람 별 평균 구하라
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

# print(midterm_score[0][2])

'''
for i in range(len(midterm_score)):
    for j in range(len(kor_score)):
        print(f'{i} {j} = {midterm_score[i][j]}')
'''       

student_score = [0, 0, 0, 0, 0]
i = 0
for subject in midterm_score:
    for score in subject:
        student_score[i] += score
        i += 1
    i = 0
else:
    a, b, c, d, e = student_score
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)
    
    
for value in student_score:
    print('{0}번째 사람의 평균점수는 {1:.2f}점입니다.'.format(i, value / 3))
    i+= 1

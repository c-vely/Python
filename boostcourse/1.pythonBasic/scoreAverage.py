# 사람 별 평균 구하라
kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

# print(midterm_score[0][2])

for i in range(len(midterm_score)):
    for j in range(len(kor_score)):
        print(f'{i} {j} = {midterm_score[i][j]}')
        

student_score = [0, 0, 0, 0, 0, ]

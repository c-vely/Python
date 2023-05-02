import bmi

weight, height = input('몸무게(kg)와 키(cm)를 입력하세요 : ').split(' ')
weight = int(weight)
height = int(height)

result = bmi.calc(weight, height)
print(f'BMI 지수는 {result : .2f}입니다.')

judge = bmi.result(result)
print (f'{judge}입니다.')

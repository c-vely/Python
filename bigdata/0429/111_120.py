'''
# 111.사용자로부터 입력받은 문자열을 두 번 출력하라. 
str = input("입력 : ")
print(str * 2)


# 112. 사용자로부터 하나의 숫자를 입력받고, 입력 받은 숫자에 10을 더해 출력하라.
num = int(input("숫자 1개 입력 : "))
print(num * 10)


# 113. 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라.
num = int(input("1개 숫자 입력 : "))

if num % 2 == 0:
    print(f'{num}는 짝수 입니다.')
else :
    print(f'{num}는 홀수 입니다.')

    
# 114. 사용자로부터 입력 받은 값에 20을 더하여 출력하라. 단, 255를 초과하는 경우 255f를 출력하라
num = int(input("1개 숫자 입력 : "))

addNum = num + 20

if addNum > 255:
    print(255)
else:
    print(addNum)

    
# 115. 사용자로부터 입력 받은 값에 20을 뺀 값을 출력하라. 단, 출력값의 범위는 0~255이다.
num = int(input("1개 숫자 입력 : "))
calNum = num -20

if calNum < 0 :
    calNum = 0
elif calNum > 255:
    calNum = 255

print(calNum)


# 116. 입력 받은 시간이 정각인지 판별하라
t = input("현재시간 : ").split(':')
if t[1] != '00':
    print('정각이 아닙니다.')
else:
    print('정각 입니다.')


# 117. 입력받은 단어가 fruit리스트에 포함되어 있는지 확인하라.
fruit = ['사과', '포도', '홍시']
f = input('좋아하는 과일은? ')

if f in fruit:
    print('정답입니다.')
else:
    print('오답입니다.')

    
# 118. 투자 경고 종목 리스트가 있을 때, 입력 받은 종목이 투자 경고 종목인지 아닌지 출력하라.
warn_investment_list = ['Microsoft', 'Google', 'Naver', 'Kakao', 'SAMSUNG', 'LG']
i = input("종목 입력 : ")

if i in warn_investment_list:
    print('투자 경고 종목입니다.')
else:
    print('투자 경고 종목이 아닙니다.')

# 119. fruit 딕셔너리에 입력한 값이 key값에 포함되어 있는지 아닌지 출력하라.
seasonFruit = {'봄':'딸기', '여름':'토마토', '가을':'사과'}

s = input('제가 좋아하는 계절은 ? ')

if s in seasonFruit.keys():
    print('ok')
else:
    print('no')

'''

# 120. 
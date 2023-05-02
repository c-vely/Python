'''
# 함수 예제 1
def add(a, b):  # a, b는 매개변수
    return a+b
print(add(3, 4))  # 3, 4는 인수


# 함수 예제 2
def say(): # 매개변수 없음
	 return 'Hi' 

def add(a, b): # 리턴없음
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))

result = add(b=5, a=3)  # b에 5, a에 3을 전달


# 함수 예제 3 : 입력 값의 갯수가 몇 개인지 모를 때
def add_many(*args): 
     result = 0 
     for i in args: 
         result = result + i 
     return result

result = add_many(1,2,3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)


# 함수 예제 4
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)


# 함수 예제 5 : 리턴 값은 언제나 1개이다
def add_and_mul(a,b): 
    return a+b, a*b   # 튜플값 하나인 (a+b, a*b)로 리턴된다.

result = add_and_mul(3,4) # 튜플값 하나인 (a+b, a*b)로 리턴된다.
print(result)

result1, result2 = add_and_mul(3, 4) # result1은 7이 되고 result2는 12가 된다.
print(result1, result2)


'''
# 함수 예제 6 : 매개변수 초기값
def say_myself(name, age, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, False)


'''
# 함수 예제 7 : 매개값이 중간에 위치하면 오류 발생
def say_myself(name, man=True, age): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.") 
    else: 
        print("여자입니다.")
'''
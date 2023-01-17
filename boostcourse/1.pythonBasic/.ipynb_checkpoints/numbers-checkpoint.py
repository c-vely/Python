import random

result = random.randint(1, 100)
print("숫자를 맞춰보세요 (1~100)")
num = 0

while(num != result):
    num = int(input(">> "))
    
    if num > result:
        print("숫자가 너무 큽니다")
    elif num < result:
        print("숫자가 너무 작습니다")
    else:
        print(f"정답입니다.입력한 숫자는 {num}입니다")


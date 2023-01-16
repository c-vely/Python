# myself
num = -1
while(num != 0):
    num = int(input("구구단 몇단을 계산할까요? (1~9) : "))
    
    if num > 0 and num <= 9:
        print(f"구구단 {num}단을 계산합니다.")
        for i in range(1, 10):
            print(f"{num} X {i} = {num * i}")
    elif num > 9:
        continue
    else:
        print("구구단 게임을 종료합니다")
        
    